from pydantic import BaseModel


class PostId(BaseModel):
    post_id: int


class StatisticsItem(BaseModel):
    post_id: int
    user_id: int
    statistics_type: str
