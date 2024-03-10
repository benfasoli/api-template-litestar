from litestar import Litestar
from litestar.di import Provide
from litestar.logging import LoggingConfig
from litestar.openapi import OpenAPIConfig

from . import dependencies, errors, logging
from .api.health.handlers import router as health_router
from .api.index.handlers import router as index_router


def create_app(postgres_uri: str, log_level: str) -> Litestar:
    logging.setup_logging(log_level)

    db_provider = dependencies.create_db_provider(postgres_uri)

    app = Litestar(
        route_handlers=[
            health_router,
            index_router,
        ],
        dependencies=dict(db=Provide(db_provider)),
        logging_config=LoggingConfig(configure_root_logger=False),
        openapi_config=OpenAPIConfig(
            title="API Template Litestar",
            version="0.1.0",
            root_schema_site="swagger",
        ),
        after_exception=[errors.log_unhandled_exception],
    )

    return app
