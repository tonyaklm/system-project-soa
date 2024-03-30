from sqlalchemy import Column, VARCHAR, PrimaryKeyConstraint, Index, INTEGER
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = 'post'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    user_id = Column(INTEGER, nullable=False)
    time = Column(sqlalchemy.types.DateTime(timezone=True), nullable=False)
    title = Column(VARCHAR, nullable=False)
    content = Column(VARCHAR, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='post_pkey'),
        Index('user_index' 'user_id')
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
