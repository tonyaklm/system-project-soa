# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: statistics_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18statistics_service.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x17\n\x04Post\x12\x0f\n\x07post_id\x18\x01 \x01(\x03\"7\n\x17ResponsePostsStatistics\x12\r\n\x05likes\x18\x01 \x01(\x03\x12\r\n\x05views\x18\x02 \x01(\x03\"+\n\x07TopUser\x12\x11\n\tauthor_id\x18\x01 \x01(\x03\x12\r\n\x05likes\x18\x02 \x01(\x03\"$\n\x0eStatisticsType\x12\x12\n\ngiven_type\x18\x01 \x01(\t\"A\n\x07TopPost\x12\x0f\n\x07post_id\x18\x01 \x01(\x03\x12\x12\n\ntop_amount\x18\x02 \x01(\x03\x12\x11\n\tauthor_id\x18\x03 \x01(\x03\x32\xa0\x01\n\x11StatisticsService\x12\x32\n\x0fPostsStatistics\x12\x05.Post\x1a\x18.ResponsePostsStatistics\x12.\n\x08TopUsers\x12\x16.google.protobuf.Empty\x1a\x08.TopUser0\x01\x12\'\n\x08TopPosts\x12\x0f.StatisticsType\x1a\x08.TopPost0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'statistics_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_POST']._serialized_start=57
  _globals['_POST']._serialized_end=80
  _globals['_RESPONSEPOSTSSTATISTICS']._serialized_start=82
  _globals['_RESPONSEPOSTSSTATISTICS']._serialized_end=137
  _globals['_TOPUSER']._serialized_start=139
  _globals['_TOPUSER']._serialized_end=182
  _globals['_STATISTICSTYPE']._serialized_start=184
  _globals['_STATISTICSTYPE']._serialized_end=220
  _globals['_TOPPOST']._serialized_start=222
  _globals['_TOPPOST']._serialized_end=287
  _globals['_STATISTICSSERVICE']._serialized_start=290
  _globals['_STATISTICSSERVICE']._serialized_end=450
# @@protoc_insertion_point(module_scope)
