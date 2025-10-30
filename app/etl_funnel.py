"""
ETL Pipeline for E-Commerce Revenue Funnel Analysis.

This script:
1. Loads raw e-commerce event data
2. Creates sessions based on 30-minute inactivity gaps
3. Identifies funnel steps (view → addtocart → transaction)
4. Generates session-level funnel flags
5. Exports artifacts for Tableau dashboard
"""
import sys
import duckdb
import pathlib as p
from utils import ARTIFACTS, get_events_file, validate_data_directory, PROJECT_ROOT


def main():
    """Run the complete ETL pipeline."""
    con = None
    try:
        # Validate data directory
        print("Validating data directory...")
        validate_data_directory()
        
        # Initialize DuckDB connection
        print("Initializing DuckDB connection...")
        con = duckdb.connect(database=":memory:")
        
        # Get events file path
        events_file = get_events_file()
        print(f"Loading events from {events_file}...")
        
        # Load events
        con.execute("""
        CREATE OR REPLACE TABLE events AS
        SELECT CAST(user_id AS VARCHAR) AS user_id,
               CAST(timestamp AS TIMESTAMP) AS ts,
               event AS event_type,
               CAST(itemid AS VARCHAR) AS sku
        FROM read_csv_auto(?);
        """, [events_file])
        
        print("Events loaded. Sessionizing...")
        
        # Sessionize: 30-min gap => new session
        con.execute("""
        CREATE OR REPLACE TABLE events_s AS
        WITH e AS (
          SELECT user_id, ts, event_type, sku,
                 CASE WHEN ts - LAG(ts) OVER (PARTITION BY user_id ORDER BY ts) > INTERVAL 30 MINUTE
                      OR LAG(ts) OVER (PARTITION BY user_id ORDER BY ts) IS NULL
                      THEN 1 ELSE 0 END AS new_session
          FROM events
        )
        SELECT *, SUM(new_session) OVER (PARTITION BY user_id ORDER BY ts ROWS UNBOUNDED PRECEDING) AS session_seq
        FROM e;
        """)
        
        print("Sessions created. Creating funnel steps...")
        
        # Ordered steps per session
        con.execute("""
        CREATE OR REPLACE TABLE funnel_steps AS
        SELECT user_id,
               CONCAT(user_id,'-',session_seq) AS session_id,
               ts, event_type, sku,
               ROW_NUMBER() OVER (PARTITION BY user_id, session_seq ORDER BY ts) AS step_order
        FROM events_s;
        """)
        
        print("Funnel steps created. Generating session flags...")
        
        # Session-level flags
        con.execute("""
        CREATE OR REPLACE TABLE funnel_session AS
        SELECT session_id,
               MAX(CASE WHEN event_type='view' THEN 1 ELSE 0 END) AS has_view,
               MAX(CASE WHEN event_type='addtocart' THEN 1 ELSE 0 END) AS has_cart,
               MAX(CASE WHEN event_type='transaction' THEN 1 ELSE 0 END) AS has_purchase
        FROM funnel_steps
        GROUP BY 1;
        """)
        
        # Export artifacts (escape single quotes in path for SQL)
        funnel_session_path = ARTIFACTS / "funnel_session.csv"
        print(f"Exporting funnel_session to {funnel_session_path}...")
        funnel_session_path_escaped = str(funnel_session_path).replace("'", "''")
        con.execute(f"""
        COPY (SELECT * FROM funnel_session) 
        TO '{funnel_session_path_escaped}' (HEADER, DELIMITER ',');
        """)
        
        # Export funnel_steps for SQL queries
        funnel_steps_path = ARTIFACTS / "funnel_steps.csv"
        print(f"Exporting funnel_steps to {funnel_steps_path}...")
        funnel_steps_path_escaped = str(funnel_steps_path).replace("'", "''")
        con.execute(f"""
        COPY (SELECT * FROM funnel_steps) 
        TO '{funnel_steps_path_escaped}' (HEADER, DELIMITER ',');
        """)
        
        # Data validation checks
        print("\nRunning data validation checks...")
        
        # Check row counts
        session_count = con.execute("SELECT COUNT(*) FROM funnel_session").fetchone()[0]
        steps_count = con.execute("SELECT COUNT(*) FROM funnel_steps").fetchone()[0]
        events_count = con.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        
        print(f"  Events loaded: {events_count:,}")
        print(f"  Funnel steps: {steps_count:,}")
        print(f"  Sessions created: {session_count:,}")
        
        # Check for null timestamps
        null_ts = con.execute("SELECT COUNT(*) FROM events WHERE ts IS NULL").fetchone()[0]
        if null_ts > 0:
            print(f"  ⚠️  Warning: {null_ts} events with NULL timestamps")
        
        # Check conversion rates
        conversions = con.execute("""
            SELECT 
                SUM(has_view) as views,
                SUM(has_cart) as carts,
                SUM(has_purchase) as purchases
            FROM funnel_session
        """).fetchone()
        
        views, carts, purchases = conversions[0], conversions[1], conversions[2]
        
        if views > 0:
            view_to_cart = (carts / views) * 100
            print(f"  View-to-cart rate: {view_to_cart:.2f}% ({carts:,}/{views:,})")
        
        if carts > 0:
            cart_to_purchase = (purchases / carts) * 100
            print(f"  Cart-to-purchase rate: {cart_to_purchase:.2f}% ({purchases:,}/{carts:,})")
        
        # Print summary
        print(f"\n✅ Pipeline complete!")
        print(f"Artifacts exported to: {ARTIFACTS}")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except duckdb.Error as e:
        print(f"❌ DuckDB Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if con is not None:
            con.close()


if __name__ == "__main__":
    main()
