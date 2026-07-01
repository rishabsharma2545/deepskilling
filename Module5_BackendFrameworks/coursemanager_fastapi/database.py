# 64. Set up SQLAlchemy with an async engine using create_async_engine. 
# Define a get_db() dependency function that yields a database session.

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///./university.db"

# 64. Create the async engine and sessionmaker
engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    expire_on_commit = False
)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session