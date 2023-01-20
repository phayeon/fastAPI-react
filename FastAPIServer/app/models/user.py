from sqlalchemy.orm import relationship
from .mixins import TimestampMixin
from ..database import Base
from sqlalchemy import Column, String


class User(Base, TimestampMixin):

    __tablename__ = "users"

    user_id = Column(String(30), primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    user_name = Column(String(20))
    token = Column(String(256))

    articles = relationship('Article', back_populates='user')

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'{self.user_id}, \n'\
            f'{self.email}, \n'\
            f'{self.password}, \n'\
            f'{self.user_name}, \n'\
            f'{self.token}, \n'\
            f'{self.create_at}, \n'\
            f'{self.updated_at}, \n'

