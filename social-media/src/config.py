from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@postgresql:5432/social_media"
    grpc_server_address: str = "post-service:8001"


settings = Settings()
