import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "local"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = "postgresql+asyncpg://admin:admin@localhost:5432/fastapi_test"
    READER_DB_URL: str = "postgresql+asyncpg://admin:admin@localhost:5432/fastapi_test"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: str = ""
    CELERY_BROKER_URL: str = "redis://redis:6379/1"
    CELERY_BACKEND_URL: str = "redis://redis:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    class Config:
        env_file = ".env"
        extra = "allow"


class TestConfig(Config):
    WRITER_DB_URL: str = "postgresql+asyncpg://admin:admin@localhost:5432/fastapi_test"
    READER_DB_URL: str = "postgresql+asyncpg://admin:admin@localhost:5432/fastapi_test"


class LocalConfig(Config): ...


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()

print(config.__dict__)
