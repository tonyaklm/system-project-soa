from sqlalchemy import Column, VARCHAR, PrimaryKeyConstraint, true
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    login = Column(VARCHAR, primary_key=True)
    first_name = Column(VARCHAR, nullable=False)
    last_name = Column(VARCHAR, nullable=False)
    date_of_birth = Column(sqlalchemy.types.DateTime(), nullable=False)
    mail = Column(VARCHAR, nullable=False)
    phone_number = Column(VARCHAR, nullable=False)
    password = Column(VARCHAR, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('login', name='user_pkey'),
    )
