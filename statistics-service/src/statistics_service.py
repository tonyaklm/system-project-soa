from common.proto import statistics_service_pb2
from common.proto import statistics_service_pb2_grpc
from database import async_session
from common.repository import repo
from tables.statistics import Statistics
from google.protobuf.empty_pb2 import Empty
from common.statistics_type import StatisticsType


class StatisticsService(statistics_service_pb2_grpc.StatisticsService):

    async def PostsStatistics(self, request: statistics_service_pb2.Post, context):
        """ Statistics for one post by its id"""

        async with async_session() as session:
            likes = await repo.select_count(Statistics.user_id,
                                            [Statistics.post_id == request.post_id,
                                             Statistics.statistics_type == StatisticsType.like.value],
                                            [Statistics.statistics_type, Statistics.post_id],
                                            session)
            views = await repo.select_count(Statistics.user_id,
                                            [Statistics.post_id == request.post_id,
                                             Statistics.statistics_type == StatisticsType.view.value],
                                            [Statistics.statistics_type, Statistics.post_id],
                                            session)

        return statistics_service_pb2.ResponsePostsStatistics(likes=likes, views=views)

    async def TopUsers(self, request: Empty, context):
        """ Top 3 users by sum amount of likes"""
        async with async_session() as session:
            posts = await repo.select_with_group_by([Statistics.author_id],
                                                    Statistics.user_id,
                                                    [Statistics.author_id],
                                                    [Statistics.statistics_type == StatisticsType.like.value],
                                                    3, session)

        for post in [row._asdict() for row in posts]:
            yield statistics_service_pb2.TopUser(author_id=post['author_id'], likes=post['selected_statistics'])

    async def TopPosts(self, request: statistics_service_pb2.StatisticsType, context):
        """ Top 5 posts by amount of likes/views"""

        async with async_session() as session:
            posts = await repo.select_with_group_by([Statistics.author_id, Statistics.post_id],
                                                    Statistics.user_id,
                                                    [Statistics.author_id, Statistics.post_id],
                                                    [Statistics.statistics_type == request.given_type],
                                                    5, session)

        for post in [row._asdict() for row in posts]:
            yield statistics_service_pb2.TopPost(post_id=post['post_id'],
                                                 top_amount=post['selected_statistics'],
                                                 author_id=post['author_id'])
