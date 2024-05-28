from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://{}:{}@postgresql:5432/social_media".format(
        os.getenv("SOCIAL_MEDIA_LOGIN"), os.getenv("SOCIAL_MEDIA_PASSWORD"))
    post_server_address: str = "post-service:8000"
    statistics_server_address: str = "statistics-service:8001"
    kafka_host: str = "kafka"
    kafka_port: int = 29092
    statistics_produce_topic: str = "post-statistics"


settings = Settings()
