#!/usr/bin/env python3
"""
Title: Enterprise OOP Log Watcher
Description: Refactored log monitoring pipeline using Object-Oriented Programming.
"""

import os
import sys
import subprocess

class LogWatcher:
    def __init__(self):
        # 1. State and Configuration
        self.alert_threshold = int(os.getenv("ALERT_THRESHOLD", "2")) # Set default to 2 to test our 2 mock errors easily!
        self.log_filename = os.getenv("LOG_TARGET", "server_ops.log")
        self.log_dir = "./logs"
        self.target_path = os.path.join(self.log_dir, self.log_filename)
        self.error_count = 0

    def initialize_environment(self):
        """Ensures the log directory exists safely."""
        try:
            os.makedirs(self.log_dir, exist_ok=True)
        except Exception as e:
            print(f"ERROR: Could not create directory {self.log_dir}: {e}")
            sys.exit(1)

    def generate_mock_logs(self):
        """Generates sample log data for testing."""
        print(f"Initializing mock log at {self.target_path}...")
        try:
            with open(self.target_path, "w") as f:
                message = "ERROR: Database connection timeout.\nINFO: System running smoothly.\nERROR: Failed to write packet."
                f.write(message)
        except Exception as e:
            print(f"Something went wrong writing logs: {e}")

    def scan_logs(self):
        """Streams the log file line by line and counts errors."""
        try:
            with open(self.target_path, "r") as f:
                for line in f:
                    if "ERROR" in line:
                        self.error_count += 1
            print(f"Scan complete. Found {self.error_count} error(s).")
        except Exception as e:
            print(f"Error reading file: {e}")

    def run_audit(self):
        """Coordinates the entire workflow pipeline."""
        self.initialize_environment()
        self.generate_mock_logs()
        self.scan_logs()

        # Check if errors meet or exceed the threshold
        if self.error_count >= self.alert_threshold:
            print(f"ALERT: Threshold breached! ({self.error_count} >= {self.alert_threshold})")
            try:
                # Run diagnostic command using subprocess
                result = subprocess.run(
                    ["uptime"], 
                    capture_output=True, 
                    text=True, 
                    check=True
                )
                output = result.stdout.strip()
                report_content = f"=== INCIDENT REPORT ===\nErrors Found: {self.error_count}\nSystem Uptime:\n{output}\n"
                
                # Write the incident report file
                report_path = os.path.join(self.log_dir, "incident_report.txt")
                with open(report_path, "w") as f:
                    f.write(report_content)
                print(f"Incident report successfully generated at {report_path}")
            except Exception as e:
                print(f"Failed to run diagnostics or write report: {e}")
        else:
            print("System stable. No incident report required.")

# This is where execution actually begins when you run the script
if __name__ == "__main__":
    watcher = LogWatcher()
    watcher.run_audit()