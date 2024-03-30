from pydantic_settings import BaseSettings

my_api = ""


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@postgresql:5432/social_media"
    grpc_server_address: str = f"{my_api}:8001"


settings = Settings()
