from common.proto import post_service_pb2
from common.proto import post_service_pb2_grpc

from typing import List, Dict
import grpc
import google.protobuf.json_format as js
import json
from config import settings
from handle.convert_codes import convert_grpc_code_into_http
from fastapi import HTTPException
import logging
from google.protobuf.empty_pb2 import Empty

_LOGGER = logging.getLogger(__name__)


class PostHandler:
    _stub = None

    def CreatePost(self, content: json):
        """ Создать новый пост"""

        protobuf_request = js.ParseDict(content, post_service_pb2.NewPost(), ignore_unknown_fields=True)
        try:
            response = self._stub.CreatePost(protobuf_request)
        except grpc.RpcError as e:
            raise HTTPException(status_code=convert_grpc_code_into_http(e), detail={
                "message": e.details()})
        response_dict = js.MessageToDict(response, preserving_proto_field_name=True)
        return response_dict

    def UpdatePost(self, content: json):
        """ Обновить пост"""
        protobuf_request = js.ParseDict(content, post_service_pb2.RequestUpdatePost(), ignore_unknown_fields=True)
        try:
            response = self._stub.UpdatePost(protobuf_request)
        except grpc.RpcError as e:
            raise HTTPException(status_code=convert_grpc_code_into_http(e), detail={
                "message": e.details()})
        response_dict = js.MessageToDict(response, preserving_proto_field_name=True)
        return response_dict

    def DeletePost(self, content: json):
        """Удалить пост"""
        protobuf_request = js.ParseDict(content, post_service_pb2.RequestDeletePost(), ignore_unknown_fields=True)

        try:
            response = self._stub.DeletePost(protobuf_request)
        except grpc.RpcError as e:
            raise HTTPException(status_code=convert_grpc_code_into_http(e), detail={
                "message": e.details()})
        response_dict = js.MessageToDict(response, preserving_proto_field_name=True)
        return response_dict

    def GetPostById(self, content: json) -> json:
        """Получить пост по его id"""

        protobuf_request = js.ParseDict(content, post_service_pb2.RequestGetPostById(), ignore_unknown_fields=True)
        try:
            response = self._stub.GetPostById(protobuf_request)
        except grpc.RpcError as e:
            raise HTTPException(status_code=convert_grpc_code_into_http(e), detail={
                "message": e.details()})
        response_dict = js.MessageToDict(response, preserving_proto_field_name=True)
        return response_dict

    def GetPosts(self, content: json) -> List[Dict]:
        """Получить посты"""

        response_iterator = self._stub.GetPosts(Empty())

        posts = []
        for post_item in list(response_iterator):
            posts.append(js.MessageToDict(post_item, preserving_proto_field_name=True))

        return posts


grpc_server_address = settings.post_server_address

channel = grpc.insecure_channel(grpc_server_address, options=(('grpc.enable_http_proxy', 0),))
stub = post_service_pb2_grpc.PostServiceStub(channel)

PostHandler._stub = stub
post_handler = PostHandler()
