from config import settings
from common.kafka.kafka_consumer import KafkaConsumerManager

kafka_conf = {"bootstrap_servers": f"{settings.kafka_host}:{settings.kafka_port}"}

kafka_consumer = KafkaConsumerManager(kafka_conf)
