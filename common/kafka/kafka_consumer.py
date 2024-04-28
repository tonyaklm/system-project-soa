from aiokafka import AIOKafkaConsumer
from collections.abc import Callable
import json
import sys
from aiokafka.errors import KafkaConnectionError


class KafkaConsumerManager(object):
    def __init__(self, conf):
        self._config = conf
        self._consumer: AIOKafkaConsumer = None
        self._consume_function: Callable[[json, ...], None] = None
        self._topic: str = None

    async def init_consumer(self, topic: str, consume_function):
        self._topic = topic

        self._consumer = AIOKafkaConsumer(self._topic, **self._config)
        self._consume_function = consume_function

    async def stop(self) -> None:
        await self._consumer.stop()

    async def consume(self) -> None:
        if not self._topic or not self._consume_function or not self._consumer:
            raise Exception("KafkaConsumer must be initialized.")

        try:

            await self._consumer.start()
        except KafkaConnectionError:
            await self._consumer.stop()
            sys.exit(0)
        try:
            async for msg in self._consumer:
                decoded_message = json.loads(msg.value.decode('utf-8'))
                await self._consume_function(decoded_message)
        finally:
            await self._consumer.stop()
