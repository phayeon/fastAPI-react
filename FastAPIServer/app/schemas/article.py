from datetime import datetime
import pydantic


class Alticle(pydantic.BaseModel):
    art_seq: int
    title: str
    content: str
    create_at: datetime
    updated_at: datetime
