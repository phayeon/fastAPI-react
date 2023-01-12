from datetime import datetime
import pytz


def currentTime():
    tz = pytz.timezone('Asia/Seoul')
    cur_time = datetime.now(tz)
    current_time = cur_time.strftime("%H:%M:%S")
    return f"{current_time}"
