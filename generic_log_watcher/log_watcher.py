#!/usr/bin/env python3
"""
Production-Ready Log Watcher Capstone Script
"""
import os
import sys
import subprocess

# 1. Get environment variables with professional defaults and casting
alert = int(os.getenv("ALERT_THRESHOLD", "3"))
log_filename = os.getenv("LOG_TARGET", "server_ops.log")
log_dir = "./logs"

# 2. Ensure the log directory exists safely
try:
    os.makedirs(log_dir, exist_ok=True)
except Exception as e:
    print(f"ERROR: Could not create directory {log_dir}: {e}")
    sys.exit(1)

target = os.path.join(log_dir, log_filename)

# 3. Automatically generate mock log data for testing
print(f"Initializing mock log file at {target}...")
mock_logs = [
    "INFO: System starting up.",
    "ERROR: Database connection timeout.",
    "WARNING: High CPU load.",
    "ERROR: Failed to write packet to socket.",
    "INFO: Routine check completed."
]
with open(target, "w") as f:
    for line in mock_logs:
        f.write(line + "\n")

# 4. Scan the log file line by line
count = 0
try:
    with open(target, "r") as f:
        for line in f:
            if "ERROR" in line:
                count += 1
    print(f"Scan complete. Found {count} error(s).")
except FileNotFoundError:
    print("Sorry, file could not be found!")
    sys.exit(1)
except Exception as e:
    print(f"Sorry, something went wrong during file reading: {e}")
    sys.exit(1)

# 5. Check threshold and execute subprocess if breached
result = None
if count >= alert:
    print(f"ALERT THRESHOLD REACHED ({count} >= {alert}). Executing diagnostic command...")
    try:
        result = subprocess.run(
            ["uptime"], 
            capture_output=True, 
            text=True, 
            check=True
        )
    except subprocess.CalledProcessError:
        print("WARNING: Failed to execute subprocess command.")
    except Exception as e:
        print(f"CRITICAL ERROR executing subprocess: {e}")

    # 6. Write incident report if subprocess succeeded
    if result and result.stdout:
        output = result.stdout.strip()
        message = f"=== INCIDENT REPORT ===\nErrors detected: {count}\nUptime Status:\n{output}\n"
        
        report_path = os.path.join(log_dir, "incident_report.txt")
        try:
            with open(report_path, "w") as f:
                f.write(message)
            print(f"Incident report successfully written to {report_path}")
        except Exception as e:
            print(f"Sorry, something went wrong writing the report: {e}")