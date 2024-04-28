from pydantic import BaseModel
from uuid import UUID


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


class SessionKey(BaseModel):
    session_key: UUID
