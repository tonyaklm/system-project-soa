from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewPost(_message.Message):
    __slots__ = ["user_id", "title", "content"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    title: str
    content: str
    def __init__(self, user_id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class ResponseNewPost(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class RequestUpdatePost(_message.Message):
    __slots__ = ["user_id", "post_id", "new_title", "new_content"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_TITLE_FIELD_NUMBER: _ClassVar[int]
    NEW_CONTENT_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    post_id: int
    new_title: str
    new_content: str
    def __init__(self, user_id: _Optional[int] = ..., post_id: _Optional[int] = ..., new_title: _Optional[str] = ..., new_content: _Optional[str] = ...) -> None: ...

class RequestDeletePost(_message.Message):
    __slots__ = ["user_id", "post_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    post_id: int
    def __init__(self, user_id: _Optional[int] = ..., post_id: _Optional[int] = ...) -> None: ...

class RequestGetPostById(_message.Message):
    __slots__ = ["user_id", "post_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    post_id: int
    def __init__(self, user_id: _Optional[int] = ..., post_id: _Optional[int] = ...) -> None: ...

class RequestGetPosts(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class PostItem(_message.Message):
    __slots__ = ["id", "user_id", "time", "title", "content"]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    time: _timestamp_pb2.Timestamp
    title: str
    content: str
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class EmptyMessage(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
