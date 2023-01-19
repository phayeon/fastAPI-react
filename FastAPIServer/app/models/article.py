from pydantic import BaseConfig
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from .mixins import TimestampMixin
from ..database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Article(Base, TimestampMixin):

    __tablename__ = "articles"

    art_seq = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(20))
    content = Column(String(20))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'))

    user = relationship('User', back_populates='articles')

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True

    def __str__(self):
        return f'글쓴이: {self.user_id}, \n ' \
               f'글번호: {self.art_seq}, \n ' \
               f'제목: {self.title} \n ' \
               f'내용: {self.content} \n' \
               f'작성일: {self.create_at} \n' \
               f'수정일: {self.updated_at} \n'
