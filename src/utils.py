"""
Utility functions and constants for the e-commerce funnel analyzer.
"""
import pathlib as p

# Path constants
RAW = p.Path("data/raw")
INTERIM = p.Path("data/interim")
ARTIFACTS = p.Path("artifacts")

# Ensure directories exist
RAW.mkdir(parents=True, exist_ok=True)
INTERIM.mkdir(parents=True, exist_ok=True)
ARTIFACTS.mkdir(parents=True, exist_ok=True)


def get_events_file():
    """Get the path to events.csv file."""
    events_path = RAW / "events.csv"
    if not events_path.exists():
        raise FileNotFoundError(
            f"events.csv not found in {RAW}. "
            "Please download the RetailRocket dataset and place events.csv in data/raw/"
        )
    return str(events_path)


def validate_data_directory():
    """Validate that data directory exists and contains required files."""
    if not RAW.exists():
        raise FileNotFoundError(
            f"Data directory {RAW} does not exist. "
            "Please create it and add your data files."
        )
    
    events_file = RAW / "events.csv"
    if not events_file.exists():
        raise FileNotFoundError(
            f"Required file events.csv not found in {RAW}. "
            "Please download the dataset and place it in data/raw/"
        )

