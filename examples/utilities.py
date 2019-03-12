import time
import datetime


def get_start_time(delta_days):
    delta = datetime.timedelta(days=delta_days)
    start_date = datetime.datetime.fromtimestamp(time.time())
    start_date = start_date - delta
    start = int(start_date.strftime("%s"))
    return start


def get_end_time():
    return int(time.time())