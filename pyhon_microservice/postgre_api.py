from psycopg import AsyncConnection, AsyncCursor
from typing import AsyncGenerator

class PostgresApi:
    def __init__(self):
        self.url: str = "postgresql://postgres:password@localhost:5432/postgres"

    async def get_cursor(self) -> AsyncGenerator[AsyncCursor]:
        async with await AsyncConnection.connect(self.url) as connection:
            async with connection.cursor() as cursor:
                yield cursor

    async def create_client(self, client_id: int):
        async with self.get_cursor() as cursor:
            pass

    async def get_client(self, client_id: int):
        async with self.get_cursor() as cursor:
            pass

    async def delete_client(self, client_id: int):
        async with self.get_cursor() as cursor:
            pass

    async def hard_update_client(self, client_id: int):
        async with self.get_cursor() as cursor:
            pass

    async def soft_update_client(self, client_id: int):
        async with self.get_cursor() as cursor:
            pass