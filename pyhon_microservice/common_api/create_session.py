from sqlalchemy.ext.asyncio import *

class CreateEngine:
    def __init__(self, url: str):
        self.__async_engine = create_async_engine(
            url=url,
            echo=True,
            pool_size=10,
            max_overflow=20,
        )

        self.__async_session = async_sessionmaker(
            bind=self.__async_engine,
            expire_on_commit=False
        )

    async def async_session_factory(self):
        async with self.__async_session() as session:
            yield session