from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Post(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class ResponsePostsStatistics(_message.Message):
    __slots__ = ("likes", "views")
    LIKES_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    likes: int
    views: int
    def __init__(self, likes: _Optional[int] = ..., views: _Optional[int] = ...) -> None: ...

class TopUser(_message.Message):
    __slots__ = ("author_id", "likes")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    author_id: int
    likes: int
    def __init__(self, author_id: _Optional[int] = ..., likes: _Optional[int] = ...) -> None: ...

class StatisticsType(_message.Message):
    __slots__ = ("given_type",)
    GIVEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    given_type: str
    def __init__(self, given_type: _Optional[str] = ...) -> None: ...

class TopPost(_message.Message):
    __slots__ = ("post_id", "top_amount", "author_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TOP_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    top_amount: int
    author_id: int
    def __init__(self, post_id: _Optional[int] = ..., top_amount: _Optional[int] = ..., author_id: _Optional[int] = ...) -> None: ...
