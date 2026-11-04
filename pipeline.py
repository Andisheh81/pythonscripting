#!/usr/bin/env python3
"""
Title: Enterprise System Health Pipeline
Description: Orchestrates environment config, subprocess execution, 
             and structured file logging with error handling.
"""

import os
import sys
import subprocess
from datetime import datetime

def load_pipeline_config():
    """Loads and type-casts environment configuration."""
    config = {
        "report_dir": os.getenv("REPORT_DIR", "./audit_reports"),
        "max_load_threshold": float(os.getenv("MAX_LOAD_THRESHOLD", "2.0"))
    }
    return config

def execute_command(cmd_list):
    """Safely runs a system command and returns stdout or None on failure."""
    try:
        result = subprocess.run(
            cmd_list, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"WARNING: Command '{' '.join(cmd_list)}' failed with code {e.returncode}")
        return None
    except Exception as e:
        print(f"CRITICAL ERROR executing subprocess: {e}")
        return None

def run_pipeline():
    print("Initializing System Health Pipeline...")
    
    # 1. Load config
    config = load_pipeline_config()
    report_dir = config["report_dir"]

    # 2. Ensure report directory exists safely
    try:
        os.makedirs(report_dir, exist_ok=True)
    except Exception as e:
        print(f"ERROR: Could not create directory {report_dir}: {e}")
        sys.exit(1)

    # 3. Gather system metrics via subprocess
    print("Gathering system metrics...")
    disk_space = execute_command(["df", "-h"])
    uptime_info = execute_command(["uptime"])

    if not disk_space or not uptime_info:
        print("ERROR: Failed to collect essential system metrics. Aborting pipeline.")
        sys.exit(1)

    # 4. Format report payload with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = os.path.join(report_dir, f"health_report_{timestamp}.txt")

    report_content = f"""=== ENTERPRISE SYSTEM HEALTH REPORT ===
Timestamp: {timestamp}
----------------------------------------
[DISK UTILIZATION (df -h)]
{disk_space}

----------------------------------------
[SYSTEM UPTIME & LOAD]
{uptime_info}
----------------------------------------
Status: Pipeline execution completed successfully.
"""

    # 5. Write structured audit file
    try:
        with open(report_filename, "w") as f:
            f.write(report_content)
        print(f"SUCCESS: Audit report written securely to {report_filename}")
    except Exception as e:
        print(f"ERROR: Failed to write report file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()