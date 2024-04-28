from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from kafka import get_kafka_producer
from aiokafka import AIOKafkaProducer
from schemas import statistics_schemas
from common.kafka.kafka_producer import send_message
from common.statistics_type import StatisticsType
from config import settings
from tables.user import User
from utils.auth import get_user
from routers.posts import get_post_by_id

router = APIRouter(prefix='/statistics')


@router.post("/like", status_code=200, summary="Post information about likes", tags=['statistics'])
async def post_likes(post: statistics_schemas.PostId, producer: AIOKafkaProducer = Depends(get_kafka_producer),
                     user: User = Depends(get_user)):
    try:
        await get_post_by_id(post.post_id, user)
    except HTTPException:
        return JSONResponse(status_code=404, content={
            "message": f"Поста {post.post_id} не существует"})

    statistics_item = statistics_schemas.StatisticsItem(post_id=post.post_id,
                                                        user_id=user.id,
                                                        statistics_type=StatisticsType.like.value)

    await send_message(producer, settings.statistics_produce_topic, statistics_item)


@router.post("/view", status_code=200, summary="Post information about views", tags=['statistics'])
async def post_likes(post: statistics_schemas.PostId, producer: AIOKafkaProducer = Depends(get_kafka_producer),
                     user: User = Depends(get_user)):
    try:
        await get_post_by_id(post.post_id, user)
    except HTTPException:
        return JSONResponse(status_code=404, content={
            "message": f"Поста {post.post_id} не существует"})

    statistics_item = statistics_schemas.StatisticsItem(post_id=post.post_id,
                                                        user_id=user.id,
                                                        statistics_type=StatisticsType.view.value)
    await send_message(producer, settings.statistics_produce_topic, statistics_item)
