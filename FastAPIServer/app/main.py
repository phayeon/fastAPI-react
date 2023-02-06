import logging
import os
import sys

from fastapi.security import APIKeyHeader
from fastapi_pagination import add_pagination
from fastapi_sqlalchemy.middleware import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from .admin.utils import currentTime
from .database import init_db
from .env import DB_url
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from .routers.user import router as user_router
from .routers.article import router as article_router
from .admin.pagination import router as pagination_router


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

API_TOKEN = "SECRET_API_TOKEN"
api_key_header = APIKeyHeader(name="Token")

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(article_router, prefix="/articles", tags=["articles"])
router.include_router(pagination_router, prefix="/pagination", tags=["pagination"])


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
add_pagination(app)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


@app.get("/")
async def home():
    return HTMLResponse(content=f"""
    <body>
    <div>
        <h1 style="width:400px;margin:50px auto">
            {currentTime()} <br/>
            현재 서버 구동 중 입니다. 
         </h1>
    </div>
    </body>
        """)


@app.get("/protected-router")
async def protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=403)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/no-match-token")
async def no_match_token():
    return {"message": f"토큰 유효시간이 지났습니다."}
