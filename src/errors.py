import logging

from litestar.types import Scope

logger = logging.getLogger(__name__)


async def log_unhandled_exception(exc: Exception, _: Scope) -> None:
    logger.error("Unhandled exception", exc_info=exc)
