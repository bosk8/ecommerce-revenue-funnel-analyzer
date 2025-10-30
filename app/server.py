"""
Backend API server for E-Commerce Revenue Funnel Analyzer UI.

This server provides REST API endpoints for:
- Pipeline execution (ETL)
- Analytics query execution
- Artifact listing and metadata

Run with: python app/server.py
Access at: http://localhost:5000
"""

import subprocess
import json
import pathlib
import csv
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pathlib import Path
import sys

# Get project root
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# App folder (where all files are)
APP_DIR = PROJECT_ROOT / "app"

app = Flask(__name__, static_folder=str(APP_DIR), static_url_path='')
CORS(app)  # Enable CORS for local development

# Paths
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
SCRIPTS_DIR = APP_DIR  # Scripts are now in app/ folder
SQL_DIR = PROJECT_ROOT / "sql"


def count_csv_rows(csv_path):
    """Count rows in a CSV file (excluding header)."""
    try:
        if not csv_path.exists():
            return None
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            return sum(1 for row in reader)
    except Exception as e:
        print(f"Error counting rows in {csv_path}: {e}")
        return None


def parse_pipeline_metrics(output):
    """Parse metrics from pipeline stdout."""
    metrics = {}
    lines = output.split('\n')
    
    for line in lines:
        if 'Events loaded:' in line:
            try:
                metrics['events_count'] = int(line.split('Events loaded:')[1].split(',')[0].strip())
            except:
                pass
        elif 'Funnel steps:' in line:
            try:
                metrics['steps_count'] = int(line.split('Funnel steps:')[1].split(',')[0].strip())
            except:
                pass
        elif 'Sessions created:' in line:
            try:
                metrics['session_count'] = int(line.split('Sessions created:')[1].split(',')[0].strip())
            except:
                pass
        elif 'View-to-cart rate:' in line:
            try:
                metrics['view_to_cart_rate'] = float(line.split('View-to-cart rate:')[1].split('%')[0].strip())
            except:
                pass
        elif 'Cart-to-purchase rate:' in line:
            try:
                metrics['cart_to_purchase_rate'] = float(line.split('Cart-to-purchase rate:')[1].split('%')[0].strip())
            except:
                pass
    
    # Also try to read from artifacts if available
    funnel_session_path = ARTIFACTS_DIR / "funnel_session.csv"
    if funnel_session_path.exists():
        try:
            with open(funnel_session_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                if rows:
                    total_views = sum(int(row.get('has_view', 0)) for row in rows)
                    total_carts = sum(int(row.get('has_cart', 0)) for row in rows)
                    total_purchases = sum(int(row.get('has_purchase', 0)) for row in rows)
                    
                    if not metrics.get('events_count'):
                        metrics['events_count'] = len(rows)  # Approximate
                    if not metrics.get('session_count'):
                        metrics['session_count'] = len(rows)
                    
                    if total_views > 0:
                        metrics['view_to_cart_rate'] = (total_carts / total_views) * 100
                    if total_carts > 0:
                        metrics['cart_to_purchase_rate'] = (total_purchases / total_carts) * 100
        except Exception as e:
            print(f"Error reading funnel_session.csv: {e}")
    
    return metrics


@app.route('/')
def index():
    """Serve index.html."""
    return send_from_directory(str(APP_DIR), 'index.html')


@app.route('/api/pipeline/run', methods=['POST'])
def run_pipeline():
    """Execute ETL pipeline."""
    try:
        # Run pipeline script
        script_path = SCRIPTS_DIR / "etl_funnel.py"
        if not script_path.exists():
            return jsonify({
                "status": "error",
                "error_code": "FileNotFoundError",
                "message": f"Pipeline script not found: {script_path}"
            }), 404
        
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode != 0:
            error_msg = result.stderr or result.stdout or "Unknown error"
            return jsonify({
                "status": "error",
                "error_code": "ExecutionError",
                "message": error_msg[:500]  # Limit error message length
            }), 500
        
        # Parse metrics from output
        metrics = parse_pipeline_metrics(result.stdout)
        
        return jsonify({
            "status": "success",
            "metrics": metrics
        })
    
    except subprocess.TimeoutExpired:
        return jsonify({
            "status": "error",
            "error_code": "TimeoutError",
            "message": "Pipeline execution timed out after 5 minutes"
        }), 500
    
    except FileNotFoundError as e:
        return jsonify({
            "status": "error",
            "error_code": "FileNotFoundError",
            "message": f"Required file not found: {str(e)}"
        }), 404
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "error_code": "Exception",
            "message": str(e)
        }), 500


@app.route('/api/analytics/run', methods=['POST'])
def run_analytics():
    """Execute analytics queries."""
    try:
        # Check prerequisite
        funnel_steps_path = ARTIFACTS_DIR / "funnel_steps.csv"
        if not funnel_steps_path.exists():
            return jsonify({
                "status": "error",
                "error_code": "FileNotFoundError",
                "message": "funnel_steps.csv not found. Please run the pipeline first."
            }), 404
        
        # Run analytics script
        script_path = SCRIPTS_DIR / "run_analytics.py"
        if not script_path.exists():
            return jsonify({
                "status": "error",
                "error_code": "FileNotFoundError",
                "message": f"Analytics script not found: {script_path}"
            }), 404
        
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode != 0:
            error_msg = result.stderr or result.stdout or "Unknown error"
            return jsonify({
                "status": "error",
                "error_code": "ExecutionError",
                "message": error_msg[:500]
            }), 500
        
        # Get row counts from exported files
        exports = []
        sku_path = ARTIFACTS_DIR / "sku_dropoff.csv"
        cohort_path = ARTIFACTS_DIR / "cohort_retention.csv"
        
        if sku_path.exists():
            rows = count_csv_rows(sku_path)
            exports.append({"file": "sku_dropoff.csv", "rows": rows})
        else:
            exports.append({"file": "sku_dropoff.csv", "rows": None})
        
        if cohort_path.exists():
            rows = count_csv_rows(cohort_path)
            exports.append({"file": "cohort_retention.csv", "rows": rows})
        else:
            exports.append({"file": "cohort_retention.csv", "rows": None})
        
        return jsonify({
            "status": "success",
            "exports": exports
        })
    
    except subprocess.TimeoutExpired:
        return jsonify({
            "status": "error",
            "error_code": "TimeoutError",
            "message": "Analytics execution timed out after 5 minutes"
        }), 500
    
    except FileNotFoundError as e:
        return jsonify({
            "status": "error",
            "error_code": "FileNotFoundError",
            "message": str(e)
        }), 404
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "error_code": "Exception",
            "message": str(e)
        }), 500


@app.route('/api/artifacts', methods=['GET'])
def get_artifacts():
    """Get list of artifacts with metadata."""
    expected_files = [
        "funnel_session.csv",
        "funnel_steps.csv",
        "sku_dropoff.csv",
        "cohort_retention.csv"
    ]
    
    files = []
    for filename in expected_files:
        file_path = ARTIFACTS_DIR / filename
        exists = file_path.exists()
        rows = None
        
        if exists:
            rows = count_csv_rows(file_path)
        
        files.append({
            "name": filename,
            "exists": exists,
            "rows": rows
        })
    
    return jsonify({"files": files})


@app.route('/api/pipeline/summary', methods=['GET'])
def get_pipeline_summary():
    """Get pipeline summary metrics from artifacts."""
    funnel_session_path = ARTIFACTS_DIR / "funnel_session.csv"
    
    if not funnel_session_path.exists():
        return jsonify({
            "status": "not_found",
            "message": "No pipeline summary available. Run the pipeline first."
        }), 404
    
    try:
        metrics = {}
        with open(funnel_session_path, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            total_views = sum(int(row.get('has_view', 0)) for row in rows)
            total_carts = sum(int(row.get('has_cart', 0)) for row in rows)
            total_purchases = sum(int(row.get('has_purchase', 0)) for row in rows)
            
            metrics['session_count'] = len(rows)
            
            # Approximate events count from steps file
            funnel_steps_path = ARTIFACTS_DIR / "funnel_steps.csv"
            if funnel_steps_path.exists():
                steps_rows = count_csv_rows(funnel_steps_path)
                if steps_rows:
                    metrics['steps_count'] = steps_rows
                    metrics['events_count'] = steps_rows  # Approximate
            
            if total_views > 0:
                metrics['view_to_cart_rate'] = (total_carts / total_views) * 100
            if total_carts > 0:
                metrics['cart_to_purchase_rate'] = (total_purchases / total_carts) * 100
        
        return jsonify({
            "status": "success",
            "metrics": metrics
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    print("Starting E-Commerce Revenue Funnel Analyzer API Server...")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Artifacts directory: {ARTIFACTS_DIR}")
    print(f"UI served at: http://127.0.0.1:5501/")
    print(f"API endpoints at: http://127.0.0.1:5501/api/")
    print("\nPress Ctrl+C to stop the server.\n")
    
    app.run(debug=True, host='127.0.0.1', port=5501)

