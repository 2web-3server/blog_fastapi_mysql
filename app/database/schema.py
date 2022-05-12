from sqlalchemy import (Column, Integer, String, DateTime, func, Enum, Boolean, Text, ForeignKey)
from sqlalchemy.orm import Session, relationship
from app.database.conn import Base


class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    blogger = Column(String(length=255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    def all_columns(self):
        return [c for c in self.__table__.columns if c.primary_key is False and c.name != "create_at"]

    def __hash__(self):
        return hash(self.id)

    def create(self, session: Session, auto_commit=False, **kwargs):
        """
        :param session:
        :param auto_commit: 자동 커밋 여부
        :param kwargs: 적재 할 데이터
        :return:
        """
        for col in self.all_columns():
            col_name = col.name
            if col_name in kwargs:
                setattr(self, col_name, kwargs.get(col_name))
        session.add(self)
        session.flush()
        if auto_commit:
            session.commit()
        return self

    def update(self, session: Session, auto_commit=False, **kwargs):
        for col in self.all_columns():
            col_name = col.name
            if col_name in kwargs:
                setattr(self, col_name, kwargs.get(col_name))
        session.add(self)
        if auto_commit:
            session.commit()
        return self

    def delete(self, session: Session, auto_commit=False):
        session.delete(self)
        if auto_commit:
            session.commit()
        return self


class Category(Base, BaseMixin):
    __tablename__ = "category"
    name = Column(String(length=100), nullable=False)
    contents = relationship("Contents", back_populates="category")


class Contents(Base, BaseMixin):
    __tablename__ = "content"
    title = Column(String(length=255), nullable=False)
    content = Column(Text(), nullable=False, default="내용을 입력 해 주세요")
    thumb = Column(String(length=1000), nullable=False, default="No Thumb")
    category_id = Column(Integer, ForeignKey("category.id"))

    category = relationship("Category", back_populates="contents")
    comments = relationship("Comments", back_populates="owner")


class Comments(Base, BaseMixin):
    __tablename__ = "comment"
    email = Column(String(length=255), nullable=False)
    content = Column(Text(), nullable=False, default="내용을 입력 해 주세요")
    password = Column(String(length=1000), nullable=False)
    content_id = Column(Integer, ForeignKey("content.id"))
    owner = relationship("Contents", back_populates="comments")
