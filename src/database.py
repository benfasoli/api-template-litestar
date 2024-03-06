from typing import Any

import psycopg


class Database:
    def __init__(self, conn: psycopg.AsyncConnection[dict[str, Any]]) -> None:
        self.conn = conn

    async def commit(self) -> None:
        await self.conn.commit()

    async def rollback(self) -> None:
        await self.conn.rollback()
