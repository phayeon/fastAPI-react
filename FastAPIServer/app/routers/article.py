from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.crud.article import ArticleCrud
from app.database import get_db
from app.schemas.article import ArticleDTO

router = APIRouter()


@router.post("/register", status_code=201)
async def register_article(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    return article_crud.add_article(request_article=dto)


@router.put("/modify", status_code=201)
async def modify_article(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.update_article(request_article=dto)


@router.delete("/remove", status_code=201)
async def remove_article(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.delete_article(request_article=dto)


@router.get("/page/{page}", status_code=201)
async def get_all_articles(page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    return {"data": article_crud.find_all_articles(page)}


@router.get("/seq/{seq}", status_code=201)
async def get_article_by_seq(dto: ArticleDTO, seq: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    art_seq = article_crud.find_article_by_seq(request_article=dto)
    if art_seq != 0:
        result = art_seq
    else:
        result = JSONResponse(status_code=400, content=dict(msg="존재 하지 않는 게시물 입니다."))
    return {"data": result}


@router.get("/id/{userid}/page/{page}", status_code=201)
async def get_articles_by_userid(userid: str, page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.find_articles_by_userid(userid=userid)


@router.get("/title/{title}/page/{page}", status_code=201)
async def get_articles_by_title(title: str, page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.find_articles_by_title(title=title)
