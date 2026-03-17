#!/usr/bin/env python3
"""Simple Supabase keep-alive script.
Run this in the background or via cron/scheduler to ping Supabase every 5 minutes.
Credentials loaded from environment variables (.env file).
"""
import os
import time
import requests
import schedule
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
API_KEY = os.getenv("SUPABASE_API_KEY")

if not SUPABASE_URL or not API_KEY:
    print("Error: Missing SUPABASE_URL or SUPABASE_API_KEY in .env file")
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
    except Exception as e:
        print(f"Ping failed: {e}")

def run_scheduler():
    """Run scheduler that pings Supabase every 5 minutes."""
    schedule.every(5).minutes.do(ping_supabase)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Scheduler started. Pinging Supabase every 5 minutes...")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
