from pydantic import BaseModel


class PostId(BaseModel):
    post_id: int


class StatisticsItem(BaseModel):
    post_id: int
    user_id: int
    statistics_type: str
    author_id: int


class PostStats(BaseModel):
    likes: int = 0
    views: int = 0


class TopUser(BaseModel):
    author_login: str
    likes: int = 0


class TopLikedPost(BaseModel):
    post_id: int
    author_login: str
    likes: int = 0


class TopViewedPost(BaseModel):
    post_id: int
    author_login: str
    views: int = 0
