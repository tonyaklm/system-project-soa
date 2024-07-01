import uvicorn
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from kafka import kafka_consumer
from config import settings
import asyncio
from consume.consume_statistics import consume_statistics
import grpc
from concurrent import futures
from common.proto import statistics_service_pb2_grpc
import statistics_service
import grpc
from concurrent import futures
import asyncio
from config import settings


async def consume():
    await kafka_consumer.init_consumer(settings.statistics_consume_topic, consume_statistics)
    asyncio.create_task(kafka_consumer.consume())


async def stop_consume():
    await kafka_consumer.stop()


async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    statistics_service_pb2_grpc.add_StatisticsServiceServicer_to_server(
        statistics_service.StatisticsService(), server)
    server.add_insecure_port(settings.insecure_port)
    await server.start()
    await server.wait_for_termination()


async def lifespan():
    await consume()
    try:
        await serve()
    finally:
        await stop_consume()


if __name__ == "__main__":
    asyncio.run(lifespan())
