from datetime import datetime
from typing import List
from uuid import UUID
import pydantic
from app.schemas.article import Article


class User(pydantic.BaseModel):
    user_id: UUID
    email: str
    password: str
    user_name: str
    token: str
    create_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True


class UserDetail(User):
    articles: List[Article] = []
