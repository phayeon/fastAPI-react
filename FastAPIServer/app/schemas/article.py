from datetime import datetime
from typing import Optional
from uuid import UUID

import pydantic


class ArticleDTO(pydantic.BaseModel):
    art_seq: Optional[int]
    title: Optional[str]
    content: Optional[str]
    user_id: Optional[UUID]
    create_at: Optional[datetime]
    updated_at: Optional[datetime]

    class config:
        orm_mode = True
