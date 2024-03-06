from collections.abc import AsyncIterator, Callable

import psycopg
from psycopg.rows import dict_row

from src.database import Database


def db_provider_factory(
    postgres_uri: str,
) -> Callable[[], AsyncIterator[Database]]:
    """Litestar adapter providing closure over postgres_uri."""

    async def db_provider() -> AsyncIterator[Database]:
        """Litestar interface adapter to manage connection lifecycle per-request."""
        conn = await psycopg.AsyncConnection.connect(postgres_uri, row_factory=dict_row)
        db = Database(conn)
        try:
            yield db
        except Exception:
            await db.rollback()
            raise
        finally:
            await conn.close()

    return db_provider
