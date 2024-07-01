from sqlalchemy import Column, VARCHAR, PrimaryKeyConstraint, INTEGER, Index
import sqlalchemy
from database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True)
    login = Column(VARCHAR, nullable=False, unique=True)
    first_name = Column(VARCHAR, nullable=False)
    last_name = Column(VARCHAR, nullable=False)
    date_of_birth = Column(sqlalchemy.types.DateTime(), nullable=False)
    mail = Column(VARCHAR, nullable=False)
    phone_number = Column(VARCHAR, nullable=False)
    password = Column(VARCHAR, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pkey'),
        Index('login_index' 'login')
    )
