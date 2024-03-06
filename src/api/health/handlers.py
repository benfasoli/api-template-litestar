from litestar import get

from src.database import Database

from . import services


@get("/health")
async def get_health(db: Database) -> None:
    assert await services.is_healthy(db)


handlers = [get_health]
