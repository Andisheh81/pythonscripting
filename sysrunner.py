#!/usr/bin/env python3
import subprocess

print("Running system diagnostics via Python...")
print("-" * 40)

# Execute 'uname -a' to get system and kernel information
# capture_output=True grabs the text, text=True makes it readable
command = ["uname", "-a"]

result = subprocess.run(command, capture_output=True, text=True)

# Print the captured standard output (stdout)
print("System Kernel Info:")
print(result.stdout.strip())

print("-" * 40)
print("Diagnostics complete!")