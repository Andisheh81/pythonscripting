import os
import sys
import subprocess
from datetime import datetime

class LogWatcher:
    def __init__(self, log_path, alert_threshold, search_keyword):
        # Store the user's provided file path and settings
        self.log_path = log_path
        self.alert_threshold = alert_threshold
        self.search_keyword = search_keyword
        self.error_count = 0

    def scan_logs(self):
        """Opens and reads the user's actual log file line by line."""
        print(f"Scanning file: {self.log_path}...")
        try:
            with open(self.log_path, "r") as f:
                for line in f:
                    if self.search_keyword in line:
                        self.error_count += 1
            print(f"Scan complete. Found {self.error_count} match(es) for '{self.search_keyword}'.")
        except FileNotFoundError:
            print(f"ERROR: The file '{self.log_path}' could not be found. Please check the path and try again.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)

    def run_audit(self):
        """Executes the scan and handles the incident report if breached."""
        self.scan_logs()

        # Check threshold
        if self.error_count >= self.alert_threshold:
            print(f"ALERT: Threshold breached! ({self.error_count} >= {self.alert_threshold})")
            try:
                # Run system diagnostics
                result = subprocess.run(["uptime"], capture_output=True, text=True, check=True)
                output = result.stdout.strip()
                
                # Generate dynamic timestamped report
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                report_filename = f"incident_{self.search_keyword.lower()}_{timestamp}.txt"
                
                report_content = f"=== INCIDENT REPORT ({self.search_keyword}) ===\nTarget File: {self.log_path}\nMatches Found: {self.error_count}\nSystem Uptime:\n{output}\n"
                
                with open(report_filename, "w") as f:
                    f.write(report_content)
                print(f"Incident report generated: {report_filename}")
            except Exception as e:
                print(f"Failed to run diagnostics or write report: {e}")
        else:
            print("System stable. No incident report required.")

# --- Interactive Entrypoint ---
if __name__ == "__main__":
    print("=== Interactive Log Audit Engine ===")
    
    # Prompt the user for their specific inputs
    user_file_path = input("Enter the path to your log file: ").strip()
    user_threshold = int(input("Enter the alert threshold (e.g., 2): ").strip())
    user_keyword = input("Enter the search keyword (e.g., ERROR): ").strip()

    # Pass user inputs into our LogWatcher class
    watcher = LogWatcher(
        log_path=user_file_path, 
        alert_threshold=user_threshold, 
        search_keyword=user_keyword
    )
    watcher.run_audit()