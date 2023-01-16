from abc import ABC
from typing import List
from sqlalchemy.orm import Session

from app.admin.security import verify_password
from app.bases.user import UserBase
from app.models.user import User
from app.schemas.user import UserDTO


class UserCrud(UserBase, ABC):
    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        self.db.add(user)
        self.db.commit()
        return "success"

    def login(self, request_user: UserDTO) -> str:
        target = self.find_user_by_id(request_user)
        verified = verify_password(plain_password=request_user.password,
                                   hashed_password=target.password)
        print(f'로그인 검증 결과 : {verified}')
        if verified:
            return target
        else:
            return None

    def update_user(self, request_user: UserDTO) -> str:
        pass

    def delete_user(self, request_user: UserDTO) -> str:
        pass

    def find_all_users(self, page: int) -> List[User]:
        print(f" page number is {page}")
        return self.db.query(User).all()

    def find_user_by_id(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.user_id == user.user_id).first()
        return db_user

    def find_user_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.email == user.email).first()
        if db_user is not None:
            return db_user.user_id
        else:
            return ""