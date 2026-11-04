#!/usr/bin/env python3
"""
Title: Environment Configuration Loader
Description: Reads system environment variables with fallback defaults.
"""

import os

def load_configuration():
    # Look for 'SERVER_ENV', default to 'development' if it doesn't exist
    env_mode = os.getenv("SERVER_ENV", "development")
    
    # Look for 'MAX_CONNECTIONS', default to '100'
    max_conn = os.getenv("MAX_CONNECTIONS", "100")

    print("=" * 40)
    print(f"SYSTEM CONFIGURATION LOADED")
    print("=" * 40)
    print(f"Environment Mode : {env_mode}")
    print(f"Max Connections  : {max_conn}")
    
    if env_mode == "production":
        print("SECURITY ALERT: Running in PRODUCTION mode. Strict logging enabled.")
    else:
        print("NOTICE: Running in DEVELOPMENT mode. Debugging tools active.")
    print("=" * 40)

if __name__ == "__main__":
    load_configuration()