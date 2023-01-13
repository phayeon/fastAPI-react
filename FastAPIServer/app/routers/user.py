from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import app.repositories.user as dao
from app.admin.utils import currentTime
from app.database import get_db
from app.schemas.user import UserDTO

router = APIRouter()


@router.post("/join")
async def join(user: UserDTO, db: Session = Depends(get_db)):
    print(f" 회원가입에 진입한 시간: {currentTime()} ")
    print(f"SignUp Inform : {user}")
    result = dao.join(user, db)
    if result =="":
        result = "failure"
    return {"data": result}


@router.post('/{id}')
async def login(id: str, item: UserDTO, db: Session = Depends(get_db)):
    dao.login(id, item, db)
    return {'data': 'Success'}


@router.put('/{id}')
async def update(id: str, item: UserDTO, db: Session = Depends(get_db)):
    dao.update(id, item, db)
    return {'data': 'Success'}


@router.delete('/{id}')
async def delete(id: str, item: UserDTO, db: Session = Depends(get_db)):
    dao.delete(id, item, db)
    return {'data': 'Success'}


@router.get('/email/{id}')
async def get_user(id: str, db: Session = Depends(get_db)):
    dao.find_user(id, db)
    return {'data': 'Success'}


@router.get('/{page}')
async def get_users(page: int, db: Session = Depends(get_db)):
    return {'data': dao.find_users(page, db)}


@router.get('/user-name/{name}/{page}')
async def get_users_by_name(search: str, page: int, db: Session = Depends(get_db)):
    dao.get_users_by_name(search, page, db)
    return {'data': 'Success'}
