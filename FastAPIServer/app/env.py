import pymysql
from sqlalchemy import create_engine

HOSTNAME = 'mydb.c50fh2ahyeku.ap-northeast-2.rds.amazonaws.com'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'qwe123!!'
DATABASE = 'mydb'
CHARSET = 'utf8'

DB_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_url, encoding="utf-8", echo=True)

conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)
