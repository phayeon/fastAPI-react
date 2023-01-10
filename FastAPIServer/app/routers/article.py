from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import app.repositories.article as dao
from app.database import get_db


router = APIRouter()


@router.get('/')
async def get_article(db: Session = Depends(get_db)):
    return {'data': dao.find_articles(db=db)}
