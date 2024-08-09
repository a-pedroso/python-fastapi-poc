import os
from dotenv import load_dotenv
from typing import Any, AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from app.config.settings import Settings

#load_dotenv()
#DATABASE_URL = os.getenv("DATABASE_URL")
settings = Settings()
DATABASE_URL = settings.DATABASE_URL

if DATABASE_URL is None:
    raise ValueError("No DATABASE_URL environment variable set.")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async def get_session() -> AsyncGenerator[Any, Any]:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
