from pydantic import BaseModel
from datetime import datetime


class BaseNewPost(BaseModel):
    title: str
    content: str


class BaseUpdatePost(BaseModel):
    post_id: int
    new_title: str
    new_content: str


class NewPostResponse(BaseModel):
    post_id: int


class PostItem(BaseModel):
    id: int
    user_id: int
    title: str
    time: datetime
    content: str


