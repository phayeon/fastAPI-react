import pymysql
from sqlalchemy import select
from app.models.user import User
from app.env import conn
from sqlalchemy.orm import Session
from app.schemas.user import UserDTO

pymysql.install_as_MySQLdb()


def find_users_legacy():
    cursor = conn.cursor()
    sql = "select * from users"
    cursor.execute(sql)
    return cursor.fetchall()


def join(userDTO: UserDTO, db: Session) -> str:
    user = User(**userDTO.dict())
    db.add(user)
    db.commit()
    return "success"


def login(userDTO: UserDTO, db: Session):
    user = User(**userDTO.dict())
    print(user.email, user.password)
    db_user = db.query(User).filter(User.email == user.email).first()
    print(f" dbUser {db_user}")
    if db_user is not None:
        if db_user.password == user.password:
            return db_user
    else:
        print("해당 이메일이 없습니다.")
        return "failure"


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
