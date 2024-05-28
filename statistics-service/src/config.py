from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://{}:{}@postgresql:5432/statistics_service".format(
        os.getenv("STATISTICS_LOGIN"), os.getenv("STATISTICS_PASSWORD"))
    kafka_host: str = "kafka"
    kafka_port: int = 29092
    insecure_port: str = "0.0.0.0:8001"
    statistics_consume_topic: str = "post-statistics"


settings = Settings()
