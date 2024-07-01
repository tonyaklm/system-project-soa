from sqlalchemy import Column, INTEGER, VARCHAR, Index
from database import Base


class Statistics(Base):
    __tablename__ = 'statistics'
    post_id = Column(INTEGER, nullable=False, primary_key=True)
    user_id = Column(INTEGER, nullable=False, primary_key=True)
    statistics_type = Column(VARCHAR, nullable=False, primary_key=True)

    __table_args__ = (
        Index('post_index' 'post_id'),
        Index('statistics_type_index' 'statistics_type')
    )
