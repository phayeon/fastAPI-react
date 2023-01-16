from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

import app.repositories.user as dao
from app.admin.security import get_hashed_password, generate_token
from app.admin.utils import currentTime
from app.crud.user import UserCrud
from app.database import get_db
from app.schemas.user import UserDTO

router = APIRouter()


@router.post("/register", status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    print(f" 회원가입에 진입한 시간: {currentTime()} ")
    print(f"SignUp Inform : {dto}")
    user_crud = UserCrud(db)
    user_id = user_crud.find_user_by_email(request_user=dto)
    if user_id == "":
        print(f'해시 전 비밀번호 {dto.password}')
        dto.password = get_hashed_password(dto.password)
        print(f'해시 전 비밀번호 {dto.password}')
        result = user_crud.add_user(request_user=dto)
    else:
        result = JSONResponse(status_code=400, content=dict(msg="이미 존재하는 이메일입니다."))
    return {"data": result}


@router.post("/join")
async def join(user: UserDTO, db: Session = Depends(get_db)):
    print(f" 회원가입에 진입한 시간: {currentTime()} ")
    print(f"SignUp Inform : {user}")
    result = dao.join(user, db)
    if result == "":
        result = "failure"
    return {"data": result}


@router.post("/login", status_code=200)
async def login(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    user_id = user_crud.find_user_by_email(request_user=dto)
    dto.user_id = user_id
    print(f"로그인 보내기 전에 확인 ID {dto.user_id}, PW {dto.password}")
    if user_id != "":
        login_user = user_crud.login(request_user=dto)
        if login_user is not None:
            print(f"로그인 성공 정보 : \n{login_user}")
            new_token = generate_token(login_user.email)
            login_user.token = new_token
            result = login_user
        else:
            print(f'로그인 실패')
            result = JSONResponse(status_code=400, content=dict(msg="비밀번호가 일치하지 않습니다."))
    else:
        result = JSONResponse(status_code=400, content=dict(msg="이메일 주소가 존재하지 않습니다."))
    return {"data": result}


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
