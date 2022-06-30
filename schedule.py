import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import datetime
from datetime import datetime

now = datetime.now()
print(now)
scheduler = BlockingScheduler()
@scheduler.scheduled_job(IntervalTrigger(days=30))
def train_model():
    os.system("redditrun.bat")


scheduler.start()