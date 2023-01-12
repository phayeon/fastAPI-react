from datetime import datetime
from uuid import UUID

import pydantic


class Article(pydantic.BaseModel):
    art_seq: int
    title: str
    content: str
    user_id: UUID
    create_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True
