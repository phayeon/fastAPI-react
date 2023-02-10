from pydantic import BaseModel


class ChatVO(BaseModel):
    class Config:
        orm_mode = True


class ChatDTO(ChatVO):
    sentence: str
