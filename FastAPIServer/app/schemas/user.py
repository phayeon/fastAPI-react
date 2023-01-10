import pydantic


class User(pydantic.BaseModel):
    user_id: str
    email: str
    password: str
    user_name: str
    token: str