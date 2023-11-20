from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from server.settings import Database

engine = create_async_engine(
    url=Database.url,
    echo=False,
)
session = sessionmaker(engine, class_=AsyncSession)


async def get_session():
    async with session() as sessionObj:
        yield sessionObj
