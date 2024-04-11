from sqlalchemy import Column, PrimaryKeyConstraint, INTEGER, Index, UUID, ForeignKeyConstraint
from sqlalchemy.orm import DeclarativeBase
from tables.User import Base


class SessionDao(Base):
    __tablename__ = 'session'
    user_id = Column(INTEGER, primary_key=True, autoincrement=False)
    session_key = Column(UUID, nullable=False, unique=True)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', name='user_session_pkey'),
        Index('session_key_index' 'session_key'),
        ForeignKeyConstraint(['user_id'], ['user.id'])
    )
