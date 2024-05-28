from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from kafka import get_kafka_producer
from aiokafka import AIOKafkaProducer
from schemas import statistics_schemas
from sqlalchemy.ext.asyncio import AsyncSession

from common.kafka.kafka_producer import send_message
from common.statistics_type import StatisticsType
from config import settings
from tables.user import User
from utils.auth import get_user
from routers.posts import get_post_by_id
from handle.statistics_handler import statistics_handler
from common.repository import repo
from utils.session import get_session
from typing import List

router = APIRouter(prefix='/statistics', tags=['statistics'])


@router.post("/like", status_code=200, summary="Post information about likes")
async def post_likes(post: statistics_schemas.PostId, producer: AIOKafkaProducer = Depends(get_kafka_producer),
                     user: User = Depends(get_user)):
    try:
        liked_post = await get_post_by_id(post.post_id)
    except HTTPException:
        return JSONResponse(status_code=404, content={
            "message": f"Поста {post.post_id} не существует"})

    statistics_item = statistics_schemas.StatisticsItem(post_id=post.post_id,
                                                        user_id=user.id,
                                                        author_id=liked_post['user_id'],
                                                        statistics_type=StatisticsType.like.value)
    await send_message(producer, settings.statistics_produce_topic, statistics_item)


@router.post("/view", status_code=200, summary="Post information about views")
async def post_likes(post: statistics_schemas.PostId, producer: AIOKafkaProducer = Depends(get_kafka_producer),
                     user: User = Depends(get_user)):
    try:
        liked_post = await get_post_by_id(post.post_id)
    except HTTPException:
        return JSONResponse(status_code=404, content={
            "message": f"Поста {post.post_id} не существует"})

    statistics_item = statistics_schemas.StatisticsItem(post_id=post.post_id,
                                                        user_id=user.id,
                                                        author_id=liked_post['user_id'],
                                                        statistics_type=StatisticsType.view.value)
    await send_message(producer, settings.statistics_produce_topic, statistics_item)


@router.get("/top/views", status_code=200, summary="Top 5 posts by amount of views",
            response_model=List[statistics_schemas.TopViewedPost])
async def top_views(session: AsyncSession = Depends(get_session)):
    posts = []
    for post in statistics_handler.get_top_posts({'given_type': StatisticsType.view.value}):
        author = await repo.select_by_criteria(User, ["id"], [int(post['author_id'])], session)
        posts.append(statistics_schemas.TopViewedPost(
            post_id=post['post_id'],
            author_login=author[0].login,
            views=post['top_amount'],
        ))
    return posts


@router.get("/top/likes", status_code=200, summary="Top 5 posts by amount of likes",
            response_model=List[statistics_schemas.TopLikedPost])
async def top_likes(session: AsyncSession = Depends(get_session)):
    posts = []
    for post in statistics_handler.get_top_posts({'given_type': StatisticsType.like.value}):
        author = await repo.select_by_criteria(User, ["id"], [int(post['author_id'])], session)
        posts.append(statistics_schemas.TopLikedPost(
            post_id=post['post_id'],
            author_login=author[0].login,
            likes=post['top_amount'],
        ))
    return posts


@router.get("/top/user", status_code=200, summary="Top 3 users by amount of likes",
            response_model=List[statistics_schemas.TopUser])
async def top_users(session: AsyncSession = Depends(get_session)):
    users = []
    for user in statistics_handler.get_top_users():
        author = await repo.select_by_criteria(User, ["id"], [int(user['author_id'])], session)
        users.append(statistics_schemas.TopUser(
            author_login=author[0].login,
            likes=user['likes'],
        ))
    return users


@router.get("/{post_id}", status_code=200, summary="Statistics for one post",
            response_model=statistics_schemas.PostStats)
async def post_statistics(post_id: int):
    try:
        await get_post_by_id(post_id)
    except HTTPException:
        return JSONResponse(status_code=404, content={
            "message": f"Поста {post_id} не существует"})
    return statistics_handler.statistics_for_post({'post_id': post_id})
