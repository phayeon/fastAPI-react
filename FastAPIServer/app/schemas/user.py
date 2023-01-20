from typing import List, Optional
from pydantic import BaseModel
from app.schemas.article import ArticleDTO


class UserVO(BaseModel):
    class Config:
        orm_mode = True


class UserDTO(BaseModel):
    user_id: Optional[str]
    email: Optional[str]
    password: Optional[str]
    user_name: Optional[str]
    token: Optional[str]
    create_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True


class UserList(UserVO):
    user_id: Optional[str]
    email: Optional[str]
    password: Optional[str]
    user_name: Optional[str]
    token: Optional[str]


class UserDetail(UserDTO):
    articles: List[ArticleDTO] = []


class UserUpdate(BaseModel):
    password: Optional[str]
    user_name: Optional[str]

    class Config:
        orm_mode = True