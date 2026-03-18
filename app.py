from fastapi import FastAPI
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
API_KEY = os.getenv("SUPABASE_API_KEY")

headers = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

endpoint = f"{SUPABASE_URL}/rest/v1/?select=1"

@app.get("/run")
def run_cron():
    try:
        r = requests.get(endpoint, headers=headers, timeout=30)

        return {
            "status": "success",
            "status_code": r.status_code,
            "time": time.strftime('%Y-%m-%d %H:%M:%S')
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}