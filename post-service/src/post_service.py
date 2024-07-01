from common.proto import post_service_pb2
from common.proto import post_service_pb2_grpc
from database import async_session
from common.repository import repo
from tables.post import Post
import logging
import google.protobuf.json_format as js
from google.protobuf.empty_pb2 import Empty
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
        async with async_session() as session:
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
        async with async_session() as session:
            existing_item = await repo.select_by_criteria(Post, ['id'], [request.post_id], session)
        if not existing_item:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f'Поста с id = {request.post_id} не существует')
            return Empty()
        if existing_item[0].user_id != request.user_id:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details(f'Для пользователя {request.user_id} нет доступа к посту {request.post_id}')
            return Empty()

        update_item = {
            'title': request.new_title,
            'content': request.new_content
        }
        async with async_session() as session:
            await repo.update_by_criteria(Post, 'id', request.post_id, update_item, session)
        return Empty()

    async def DeletePost(self, request, context):
        """Удалить пост"""

        existing_item = None
        async with async_session() as session:
            existing_item = await repo.select_by_criteria(Post, ['id'], [request.post_id], session)
        if not existing_item:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f'Поста с id = {request.post_id} не существует')
            return Empty()
        if existing_item[0].user_id != request.user_id:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details(f'Для пользователя {request.user_id} нет доступа к посту {request.post_id}')
            return Empty()

        async with async_session() as session:
            await repo.delete_item(Post, 'id', request.post_id, session)
        return Empty()

    async def GetPostById(self, request, context):
        """Получить пост по его id"""
        post_item = None
        async with async_session() as session:
            post_item = await repo.select_by_criteria(Post, ['id'], [request.post_id], session)
            if not post_item:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f'Поста с id = {request.post_id} не существует')
                return post_service_pb2.PostItem()
        post_item_dict = post_item[0].as_dict()
        post_item_dict['time'] = post_item_dict['time'].isoformat()

        return js.ParseDict(post_item_dict, post_service_pb2.PostItem())

    async def GetPosts(self, request, context):
        """Получить посты"""
        post_items = []
        async with async_session() as session:
            post_items = await repo.select_all(Post, session)

        for i in range(len(post_items)):
            post_item_dict = post_items[i].as_dict()
            post_item_dict['time'] = post_item_dict['time'].isoformat()

            yield js.ParseDict(post_item_dict, post_service_pb2.PostItem())
