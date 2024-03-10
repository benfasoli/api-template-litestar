from litestar import Litestar
from litestar.di import Provide
from litestar.openapi import OpenAPIConfig

from . import dependencies, logging
from .api.health.handlers import router as health_router
from .api.index.handlers import router as index_router


def create_app(postgres_uri: str, log_level: str) -> Litestar:
    logging.configure_logger(log_level)

    db_provider = dependencies.db_provider_factory(postgres_uri)

    app = Litestar(
        route_handlers=[
            health_router,
            index_router,
        ],
        dependencies=dict(db=Provide(db_provider)),
        openapi_config=OpenAPIConfig(
            title="API Template Litestar",
            version="0.1.0",
            root_schema_site="swagger",
        ),
    )
    return app
