import uvicorn
from fastapi import FastAPI
from routers import users, posts, statistics
from fastapi_pagination import add_pagination
from contextlib import asynccontextmanager
from kafka import kafka_producer
from config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kafka_producer.init_producer(settings.statistics_produce_topic)
    try:
        yield
    finally:
        await kafka_producer.stop()


app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(statistics.router)

add_pagination(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
