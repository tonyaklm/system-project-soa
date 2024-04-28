from aiokafka import AIOKafkaProducer
from contextlib import asynccontextmanager
import json


class KafkaProducerManager(object):
    def __init__(self, conf):
        self._config = conf
        self._producer: AIOKafkaProducer = None
        self._topic: str = None

    async def init_producer(self, topic: str):
        self._topic = topic
        self._producer = AIOKafkaProducer(**self._config)
        await self.start()

    async def start(self) -> None:
        await self._producer.start()

    async def stop(self) -> None:
        await self._producer.stop()

    @asynccontextmanager
    async def session(self) -> AIOKafkaProducer:
        if not self._producer:
            raise Exception("KafkaProducerSession must be initialized.")

        yield self._producer


async def send_message(producer: AIOKafkaProducer, topic: str, value: str):
    await producer.send(
        topic=topic,
        value=json.dumps(value.model_dump()).encode(encoding="utf-8"),
        )