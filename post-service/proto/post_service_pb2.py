# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: post_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12post_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto\":\n\x07NewPost\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"\"\n\x0fResponseNewPost\x12\x0f\n\x07post_id\x18\x01 \x01(\x03\"]\n\x11RequestUpdatePost\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\x12\x11\n\tnew_title\x18\x03 \x01(\t\x12\x13\n\x0bnew_content\x18\x04 \x01(\t\"5\n\x11RequestDeletePost\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\"6\n\x12RequestGetPostById\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\"\"\n\x0fRequestGetPosts\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\"q\n\x08PostItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07user_id\x18\x02 \x01(\x03\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\"\x0e\n\x0c\x45mptyMessage2\xf3\x01\n\x0bPostService\x12(\n\nCreatePost\x12\x08.NewPost\x1a\x10.ResponseNewPost\x12/\n\nUpdatePost\x12\x12.RequestUpdatePost\x1a\r.EmptyMessage\x12/\n\nDeletePost\x12\x12.RequestDeletePost\x1a\r.EmptyMessage\x12-\n\x0bGetPostById\x12\x13.RequestGetPostById\x1a\t.PostItem\x12)\n\x08GetPosts\x12\x10.RequestGetPosts\x1a\t.PostItem0\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'post_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_NEWPOST']._serialized_start=55
  _globals['_NEWPOST']._serialized_end=113
  _globals['_RESPONSENEWPOST']._serialized_start=115
  _globals['_RESPONSENEWPOST']._serialized_end=149
  _globals['_REQUESTUPDATEPOST']._serialized_start=151
  _globals['_REQUESTUPDATEPOST']._serialized_end=244
  _globals['_REQUESTDELETEPOST']._serialized_start=246
  _globals['_REQUESTDELETEPOST']._serialized_end=299
  _globals['_REQUESTGETPOSTBYID']._serialized_start=301
  _globals['_REQUESTGETPOSTBYID']._serialized_end=355
  _globals['_REQUESTGETPOSTS']._serialized_start=357
  _globals['_REQUESTGETPOSTS']._serialized_end=391
  _globals['_POSTITEM']._serialized_start=393
  _globals['_POSTITEM']._serialized_end=506
  _globals['_EMPTYMESSAGE']._serialized_start=508
  _globals['_EMPTYMESSAGE']._serialized_end=522
  _globals['_POSTSERVICE']._serialized_start=525
  _globals['_POSTSERVICE']._serialized_end=768
# @@protoc_insertion_point(module_scope)