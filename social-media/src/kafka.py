from config import settings
from common.kafka.kafka_producer import KafkaProducerManager

kafka_conf = {"bootstrap_servers": f"{settings.kafka_host}:{settings.kafka_port}"}

kafka_producer = KafkaProducerManager(kafka_conf)


async def get_kafka_producer():
    async with kafka_producer.session() as session:
        yield session
