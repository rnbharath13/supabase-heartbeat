#!/usr/bin/env python3
"""Supabase keep-alive script.
Runs once and exits (for cron/scheduler use).
"""

import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
API_KEY = os.getenv("SUPABASE_API_KEY")

if not SUPABASE_URL or not API_KEY:
    print("Error: Missing SUPABASE_URL or SUPABASE_API_KEY")
    exit(1)

headers = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

endpoint = f"{SUPABASE_URL}/rest/v1/users?select=id,employee_id,full_name,email,role&limit=1"


def ping_supabase():
    try:
        r = requests.get(endpoint, headers=headers, timeout=30)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] status={r.status_code}")
        print(r.text)

        if r.status_code != 200:
            print("Warning: Unexpected response from Supabase")

    except Exception as e:
        print(f"Ping failed: {e}")


if __name__ == "__main__":
    ping_supabase()