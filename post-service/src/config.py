from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://{}:{}@postgresql:5432/post_service".format(
        os.getenv("POST_LOGIN"), os.getenv("POST_PASSWORD"))
    insecure_port: str = "0.0.0.0:8000"


settings = Settings()