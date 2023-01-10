import pymysql
from app.models.user import User
from app.env import conn
from sqlalchemy.orm import Session

pymysql.install_as_MySQLdb()


def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()


def join(item: User, db: Session):
    return None


def login(id: str, item: User, db: Session):
    return None


def update(id: str, item: User, db: Session):
    return None


def delete(id: str, item: User, db: Session):
    return None


def find_user(id: str, db: Session):
    return None


def find_users(page: int, db: Session):
    return db.query(User).all()


def get_users_by_name(search: str, page: int, db: Session):
    return None
