import uvicorn
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from kafka import kafka_consumer
from config import settings
import asyncio
from consume.consume_statistics import consume_statistics


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kafka_consumer.init_consumer(settings.statistics_consume_topic, consume_statistics)
    asyncio.create_task(kafka_consumer.consume())

    yield
    await kafka_consumer.stop()


app = FastAPI(lifespan=lifespan)


@app.post("/", status_code=200)
async def root(request: Request):
    return


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
