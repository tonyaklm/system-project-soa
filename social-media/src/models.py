from pydantic import BaseModel
from datetime import datetime


class BaseUser(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    mail: str
    phone_number: str
    login: str
    password: str


class BaseUpdateData(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    mail: str
    phone_number: str
    login: str


class BaseAuthorizationData(BaseModel):
    login: str
    password: str


class BaseNewPost(BaseModel):
    login: str
    title: str
    content: str
    password: str


class BaseUpdatePost(BaseModel):
    login: str
    post_id: int
    new_title: str
    new_content: str
    password: str


class BaseDeletePost(BaseModel):
    login: str
    post_id: int
    password: str


class RequestGetPostById(BaseModel):
    user_login: str
    post_id: int
    password: str


class RequestGetPosts(BaseModel):
    login: str
    password: str


class NewPostResponse(BaseModel):
    post_id: int


class PostItem(BaseModel):
    id: int
    user_id: int
    title: str
    time: datetime
    content: str
