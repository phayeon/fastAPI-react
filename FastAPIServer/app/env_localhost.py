import pymysql
from sqlalchemy import create_engine

HOSTNAME = 'host.docker.internal'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'mydb'
CHARSET = 'utf8'

DB_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_url, encoding="utf-8", echo=True)

conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)
