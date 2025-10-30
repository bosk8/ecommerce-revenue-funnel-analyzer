"""
Execute analytics SQL queries and export results to artifacts.
"""
import sys
import duckdb
import pathlib as p
from utils import ARTIFACTS, PROJECT_ROOT


def run_sql_query(sql_file, output_file):
    """Execute a SQL file and export results to CSV.
    
    Args:
        sql_file: Name of SQL file in sql/ directory
        output_file: Name of output CSV file for artifacts/ directory
        
    Raises:
        FileNotFoundError: If SQL file or required data files are missing
        duckdb.Error: If SQL execution fails
    """
    sql_path = PROJECT_ROOT / "sql" / sql_file
    output_path = ARTIFACTS / output_file
    
    if not sql_path.exists():
        raise FileNotFoundError(f"SQL file not found: {sql_path}")
    
    print(f"Executing {sql_file}...")
    con = None
    try:
        con = duckdb.connect(database=":memory:")
        
        # Read SQL file
        with open(sql_path, 'r', encoding='utf-8') as f:
            sql = f.read()
        
        # Split into statements (separated by semicolons)
        statements = [s.strip() for s in sql.split(';') if s.strip() and not s.strip().startswith('--')]
        
        if not statements:
            raise ValueError(f"SQL file {sql_file} is empty or contains no valid statements")
        
        # Execute setup statements (CREATE TABLE, etc.)
        for stmt in statements[:-1]:
            if stmt:
                # Update path references to use absolute paths
                stmt = stmt.replace("'artifacts/", f"'{ARTIFACTS}/")
                con.execute(stmt)
        
        # Last statement should be the SELECT query
        select_query = statements[-1] if statements else ""
        
        if not select_query:
            raise ValueError(f"SQL file {sql_file} contains no SELECT query")
        
        # Execute query and export (escape single quotes in path for SQL)
        output_path_escaped = str(output_path).replace("'", "''")
        con.execute(f"""
        COPY (
            {select_query}
        ) TO '{output_path_escaped}' (HEADER, DELIMITER ',');
        """)
        
        # Get row count
        result = con.execute(f"SELECT COUNT(*) FROM ({select_query})").fetchone()
        print(f"✅ Exported {result[0]} rows to {output_path}")
        
    except duckdb.Error as e:
        print(f"❌ DuckDB Error executing {sql_file}: {e}", file=sys.stderr)
        raise
    finally:
        if con is not None:
            con.close()


def main():
    """Run all analytics queries."""
    try:
        print("Running analytics queries...\n")
        
        # Ensure funnel_steps.csv exists
        funnel_steps_path = ARTIFACTS / "funnel_steps.csv"
        if not funnel_steps_path.exists():
            raise FileNotFoundError(
                f"funnel_steps.csv not found in {ARTIFACTS}. "
                "Please run 'python src/etl_funnel.py' first."
            )
        
        # Run SKU drop-off analysis
        run_sql_query("sku_dropoff.sql", "sku_dropoff.csv")
        
        # Run cohort retention analysis
        run_sql_query("cohort_retention.sql", "cohort_retention.csv")
        
        print("\n✅ All analytics queries complete!")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except duckdb.Error as e:
        print(f"❌ DuckDB Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
