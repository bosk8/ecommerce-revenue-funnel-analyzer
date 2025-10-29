import os
import subprocess
import pytest
from src.utils import ARTIFACTS, RAW

@pytest.fixture(scope="module")
def setup_test_data():
    """Create dummy data for testing."""
    RAW.mkdir(parents=True, exist_ok=True)
    events_data = """user_id,timestamp,event,itemid
1,2023-01-01 10:00:00,view,101
1,2023-01-01 10:01:00,addtocart,101
1,2023-01-01 10:02:00,transaction,101
2,2023-01-01 11:00:00,view,102
"""
    events_file = RAW / "events.csv"
    with open(events_file, "w") as f:
        f.write(events_data)

    # Run the ETL pipeline to generate the necessary artifacts
    subprocess.run(["python", "src/etl_funnel.py"], check=True)

    yield

    os.remove(events_file)
    os.remove(ARTIFACTS / "funnel_session.csv")
    os.remove(ARTIFACTS / "funnel_steps.csv")
    os.remove(ARTIFACTS / "sku_dropoff.csv")
    os.remove(ARTIFACTS / "cohort_retention.csv")

def test_run_analytics_runs_successfully(setup_test_data):
    """Test that run_analytics.py runs without errors."""
    result = subprocess.run(["python", "src/run_analytics.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "All analytics queries complete!" in result.stdout
    assert os.path.exists(ARTIFACTS / "sku_dropoff.csv")
    assert os.path.exists(ARTIFACTS / "cohort_retention.csv")
