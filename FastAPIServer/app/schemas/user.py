from datetime import datetime
from typing import List, Optional
from uuid import UUID
import pydantic
from app.schemas.article import Article


class UserDTO(pydantic.BaseModel):
    user_id: Optional[str]
    email: Optional[str]
    password: Optional[str]
    user_name: Optional[str]
    token: Optional[str]
    create_at: Optional[str]
    updated_at: Optional[str]

    class config:
        orm_mode = True


class UserDetail(UserDTO):
    articles: List[Article] = []
