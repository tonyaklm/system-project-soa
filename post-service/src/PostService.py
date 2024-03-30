import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'proto'))
from proto import post_service_pb2
from proto import post_service_pb2_grpc
from start_session import get_session
from common.Repository import repo
from Post import Post
import logging
import google.protobuf.json_format as js
from sqlalchemy.exc import DataError, DBAPIError

logging.basicConfig(level=logging.DEBUG)
from datetime import datetime
import pytz
import grpc


class PostService(post_service_pb2_grpc.PostService):

    async def CreatePost(self, request, context):
        """ Создать новый пост"""
        moscow_tz = pytz.timezone("Europe/Moscow")
        creation_time = datetime.now(moscow_tz)
        new_item = {
            'user_id': request.user_id,
            'time': creation_time,
            'title': request.title,
            'content': request.content
        }
        new_post = None
        async for session in get_session():
            try:
                new_post = await repo.post_item(Post, new_item, session)
            except DBAPIError or DataError:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details('Переданы неверные данные')
                return post_service_pb2.ResponseNewPost()

        return post_service_pb2.ResponseNewPost(post_id=new_post.id)

    async def UpdatePost(self, request, context):
        """ Обновить пост"""
        existing_item = None
        async for session in get_session():
            existing_item = await repo.select_by_criteria(Post, ['id'], [request.post_id], session)
        if not existing_item:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f'Поста с id = {request.post_id} не существует')
            return post_service_pb2.EmptyMessage()
        if existing_item[0].user_id != request.user_id:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details(f'Для пользователя {request.user_id} нет доступа к посту {request.post_id}')
            return post_service_pb2.EmptyMessage()

        update_item = {
            'title': request.new_title,
            'content': request.new_content
        }
        async for session in get_session():
            await repo.update_by_criteria(Post, 'id', request.post_id, update_item, session)
        return post_service_pb2.EmptyMessage()

    async def DeletePost(self, request, context):
        """Удалить пост"""

        existing_item = None
        async for session in get_session():
            existing_item = await repo.select_by_criteria(Post, ['id'], [request.post_id], session)
        if not existing_item:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f'Поста с id = {request.post_id} не существует')
            return post_service_pb2.EmptyMessage()
        if existing_item[0].user_id != request.user_id:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details(f'Для пользователя {request.user_id} нет доступа к посту {request.post_id}')
            return post_service_pb2.EmptyMessage()

        async for session in get_session():
            await repo.delete_item(Post, 'id', request.post_id, session)
        return post_service_pb2.EmptyMessage()

    async def GetPostById(self, request, context):
        """Получить пост по его id"""
        post_item = None
        async for session in get_session():
            post_item = await repo.select_by_criteria(Post, ['id'], [request.post_id], session)
            if not post_item:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f'Поста с id = {request.post_id} не существует')
                return post_service_pb2.PostItem()
            if post_item[0].user_id != request.user_id:
                context.set_code(grpc.StatusCode.PERMISSION_DENIED)
                context.set_details(f'Для пользователя {request.user_id} нет доступа к посту {request.post_id}')
                return post_service_pb2.PostItem()
        post_item_dict = post_item[0].as_dict()
        post_item_dict['time'] = post_item_dict['time'].isoformat()

        return js.ParseDict(post_item_dict, post_service_pb2.PostItem())

    async def GetPosts(self, request, context):
        """Получить посты"""
        post_items = []
        async for session in get_session():
            post_items = await repo.select_by_criteria(Post, ['user_id'], [request.user_id], session)

        for i in range(len(post_items)):
            post_item_dict = post_items[i].as_dict()
            post_item_dict['time'] = post_item_dict['time'].isoformat()

            yield js.ParseDict(post_item_dict, post_service_pb2.PostItem())
