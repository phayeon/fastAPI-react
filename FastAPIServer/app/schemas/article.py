from datetime import datetime
from typing import Optional
from uuid import UUID

import pydantic


class ArticleDTO(pydantic.BaseModel):
    art_seq: Optional[int]
    title: Optional[str]
    content: Optional[str]
    create_at: Optional[str]
    updated_at: Optional[str]
    user_id: Optional[str]

    class config:
        orm_mode = True
