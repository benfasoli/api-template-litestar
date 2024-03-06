import psycopg

from src.database import Database


async def is_healthy(db: Database) -> bool:
    try:
        async with db.conn.cursor() as cursor:
            await cursor.execute("SELECT 1")
        return True
    except psycopg.Error:
        return False
