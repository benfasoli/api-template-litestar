import logging

from litestar import Litestar
from litestar.di import Provide
from litestar.openapi import OpenAPIConfig

from . import dependencies
from .api.health.handlers import handlers as health_handlers
from .api.index.handlers import handlers as index_handlers


def _configure_logger(level: str) -> None:
    logging.basicConfig(level=level)


def create_app(postgres_uri: str, log_level: str) -> Litestar:
    _configure_logger(log_level)

    db_provider = dependencies.db_provider_factory(postgres_uri)

    app = Litestar(
        route_handlers=[
            *health_handlers,
            *index_handlers,
        ],
        dependencies=dict(db=Provide(db_provider)),
        openapi_config=OpenAPIConfig(
            title="API Template Litestar",
            version="0.1.0",
            root_schema_site="swagger",
        ),
    )
    return app
