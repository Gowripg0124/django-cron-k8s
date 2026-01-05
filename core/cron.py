from datetime import datetime

def my_cron_job():
    print(f"[DJANGO CRON] Job ran at {datetime.now()}", flush=True)
