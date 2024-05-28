from common.proto import statistics_service_pb2
from common.proto import statistics_service_pb2_grpc

import grpc
import google.protobuf.json_format as js
import json
from config import settings
from handle.convert_codes import convert_grpc_code_into_http
from fastapi import HTTPException
import logging
from google.protobuf.empty_pb2 import Empty

_LOGGER = logging.getLogger(__name__)


class StatisticsHandler:
    _stub = None

    def statistics_for_post(self, content: json):
        """ Statistics for one post by its id"""

        protobuf_request = statistics_service_pb2.Post(post_id=content.get('post_id', None))
        try:
            response = self._stub.PostsStatistics(protobuf_request)
        except grpc.RpcError as e:
            raise HTTPException(status_code=convert_grpc_code_into_http(e), detail={
                "message": e.details()})
        response_dict = js.MessageToDict(response, preserving_proto_field_name=True)
        return response_dict

    def get_top_users(self):
        """Top 3 users by their amount of likes"""

        response_iterator = self._stub.TopUsers(Empty())
        users = []
        for user in list(response_iterator):
            users.append(js.MessageToDict(user, preserving_proto_field_name=True))
            print(user)

        return users

    def get_top_posts(self, content: json):
        """Top 5 posts by their amount of likes/view"""

        protobuf_request = statistics_service_pb2.StatisticsType(given_type=content.get('given_type', None))
        response_iterator = self._stub.TopPosts(protobuf_request)
        posts = []
        for post_item in list(response_iterator):
            posts.append(js.MessageToDict(post_item, preserving_proto_field_name=True))

        return posts


grpc_server_address = settings.statistics_server_address

channel = grpc.insecure_channel(grpc_server_address, options=(('grpc.enable_http_proxy', 0),))
stub = statistics_service_pb2_grpc.StatisticsServiceStub(channel)

StatisticsHandler._stub = stub
statistics_handler = StatisticsHandler()
