from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from .mixins import TimestampMixin
from ..database import Base
from sqlalchemy import Column, String


class User(Base, TimestampMixin):

    __tablename__ = "users"
    user_id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    user_name = Column(String(20))
    token = Column(String(20))

    articles = relationship('Article', back_populates='user')

    class Config:
        arbitrary_types_allowed = True
