import pymysql
from app.models.article import Article
from sqlalchemy.orm import Session

pymysql.install_as_MySQLdb()


def find_articles(db: Session):
    return db.query(Article).all()
