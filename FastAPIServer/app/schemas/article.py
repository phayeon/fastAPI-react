from datetime import datetime
from typing import List
import pydantic
from app.schemas.user import User


class Article(pydantic.BaseModel):
    art_seq: int
    title: str
    content: str
    create_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True
