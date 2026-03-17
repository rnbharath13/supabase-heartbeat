# Supabase Keep-Alive Script

A simple Python script that pings your Supabase database every 10 minutes to prevent project pause due to inactivity.

## Setup (Secure)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure credentials:**
   - Copy `.env.example` to `.env`
   - Edit `.env` and add your Supabase credentials:
     ```
     SUPABASE_URL=https://your-project.supabase.co
     SUPABASE_API_KEY=your-api-key
     ```
   - `.env` is ignored by git and will NOT be committed

3. **Test the script:**
   ```bash
   python keepalive.py
   ```

4. **Scheduled Task (already created):**
   - Windows: Task Scheduler will run the script every 10 minutes
   - Linux/macOS: Use cron (add to crontab: `*/10 * * * * /usr/bin/python3 /path/to/keepalive.py`)

## Security Notes

- **Never commit `.env` file** - it contains sensitive API keys
- `.gitignore` blocks `.env` from being committed
- `.env.example` shows the format without exposing secrets
- Only include `requirements.txt`, `.env.example`, `.gitignore`, and `keepalive.py` in git
