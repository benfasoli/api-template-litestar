from litestar import Router, get

from src.database import Database

from . import services


@get("/")
async def get_health(db: Database) -> None:
    assert await services.is_healthy(db)


router = Router(path="/health", route_handlers=[get_health])
