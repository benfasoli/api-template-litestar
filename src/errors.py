import logging

from litestar.types import Scope

logger = logging.getLogger(__name__)


async def log_unhandled_exception(exc: Exception, _: Scope) -> None:
    """Pass unhandled exceptions to log formatter.

    Uncaught exception tracebacks are not logged by Litestar by default. The logging
    interface is likely to change in Litestar v3.0, see:
        https://github.com/litestar-org/litestar/issues/2858

    This ensures unhandled exceptions are logged using the same formatter as other
    non-error log messages.
    """
    logger.error("Unhandled exception", exc_info=exc)
