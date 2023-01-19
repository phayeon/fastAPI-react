from datetime import datetime, timedelta
from sqlalchemy import TIMESTAMP as Timestamp, Column


class TimestampMixin(object):
    kst = datetime.utcnow() + timedelta(hours=9)    # 한국 표준시인 KST는 UTC로부터 9시간을 더하면 된다
    now = kst.strftime("%Y-%m-%d %H:%M:%S")
    create_at = Column(Timestamp, nullable=False, default=now)
    updated_at = Column(Timestamp, nullable=False,  default=now)
