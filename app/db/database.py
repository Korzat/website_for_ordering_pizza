from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ..core.config import settings

engine = create_async_engine(f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}")

session = async_sessionmaker(engine, expire_on_commit=False)
