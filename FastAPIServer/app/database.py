from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.env import engine
import pymysql
import pymysql.cursors
import logging

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = SessionLocal.query_property()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e


class Database:
    '''
    database 제어
    '''

    def __init__(self, host, user, password, db_name, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.db_name = db_name
        self.conn = None

    # DB 연결
    def connect(self):
        if self.conn != None:
            return

        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db_name,
            charset=self.charset
        )

    # DB 연결 닫기
    def close(self):
        if self.conn is None:
            return

        if not self.conn.open:
            self.conn = None
            return
        self.conn.close()
        self.conn = None

    # SQL 구문 실행
    def execute(self, sql):
        last_row_id = -1
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
            self.conn.commit()
            last_row_id = cursor.lastrowid
            # logging.debug("excute last_row_id : %d", last_row_id)
        except Exception as ex:
            logging.error(ex)

        finally:
            return last_row_id

    # SELECT 구문 실행 후, 단 1개의 데이터 ROW만 불러옴
    def select_one(self, sql):
        result = None

        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except Exception as ex:
            logging.error(ex)

        finally:
            return result

    # SELECT 구문 실행 후, 전체 데이터 ROW만 불러옴
    def select_all(self, sql):
        result = None

        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception as ex:
            logging.error(ex)

        finally:
            return result
