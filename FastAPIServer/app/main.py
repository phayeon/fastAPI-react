import logging
import os
import sys

from fastapi.security import APIKeyHeader
from fastapi_sqlalchemy.middleware import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from .database import init_db
from .env import DB_url

from fastapi import FastAPI, APIRouter, HTTPException, Depends
from .routers.user import router as user_router
from .routers.article import router as article_router

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
API_TOKEN = "SECRET_API_TOKEN"
api_key_header = APIKeyHeader(name="Token")

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(article_router, prefix="/articles", tags=["articles"])

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.router.redirect_slashes = False
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_url)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


@app.get("/protected-router")
async def protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=403)
    return {"잘못된": "경로입니다."}


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def root():
    return {"message ": " Welcome Fastapi"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
