from datetime import datetime
from typing import List, Optional
from uuid import UUID
import pydantic
from app.schemas.article import Article


class User(pydantic.BaseModel):
    user_id: Optional[UUID]
    email: str
    password: str
    user_name: str
    token: Optional[str]
    create_at: Optional[datetime]
    updated_at: Optional[datetime]

    class config:
        orm_mode = True


class UserDetail(User):
    articles: List[Article] = []
