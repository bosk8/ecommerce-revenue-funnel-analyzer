"""
Execute analytics SQL queries and export results to artifacts.
"""
import duckdb
import pathlib as p
from utils import ARTIFACTS


def run_sql_query(sql_file, output_file):
    """Execute a SQL file and export results to CSV."""
    sql_path = p.Path(f"sql/{sql_file}")
    output_path = ARTIFACTS / output_file
    
    if not sql_path.exists():
        raise FileNotFoundError(f"SQL file not found: {sql_path}")
    
    print(f"Executing {sql_file}...")
    con = duckdb.connect(database=":memory:")
    
    # Read SQL file
    with open(sql_path, 'r') as f:
        sql = f.read()
    
    # Split into statements (separated by semicolons)
    statements = [s.strip() for s in sql.split(';') if s.strip() and not s.strip().startswith('--')]
    
    # Execute setup statements (CREATE TABLE, etc.)
    for stmt in statements[:-1]:
        if stmt:
            con.execute(stmt)
    
    # Last statement should be the SELECT query
    select_query = statements[-1] if statements else ""
    
    # Execute query and export
    con.execute(f"""
    COPY (
        {select_query}
    ) TO '{output_path}' (HEADER, DELIMITER ',');
    """)
    
    # Get row count
    result = con.execute(f"SELECT COUNT(*) FROM ({select_query})").fetchone()
    print(f"✅ Exported {result[0]} rows to {output_path}")
    
    con.close()


def main():
    """Run all analytics queries."""
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


if __name__ == "__main__":
    main()

