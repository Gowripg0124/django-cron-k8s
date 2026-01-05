from datetime import datetime

def my_cron_job():
    print(f"[DJANGO CRON] Job executed at {datetime.now()}")
