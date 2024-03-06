from litestar import Litestar
from litestar.di import Provide
from litestar.logging import LoggingConfig
from litestar.openapi import OpenAPIConfig

from . import dependencies
from .health import handlers as health_handlers
from .index import handlers as index_handlers


def init_app() -> Litestar:
    from . import environment

    db_provider = dependencies.db_provider_factory(environment.POSTGRES_URI)

    app = Litestar(
        route_handlers=[
            health_handlers.get_health,
            index_handlers.get_index,
        ],
        dependencies=dict(db=Provide(db_provider)),
        logging_config=LoggingConfig(root=dict(level=environment.LOG_LEVEL)),
        openapi_config=OpenAPIConfig(
            title="API Template Litestar",
            version="0.1.0",
            root_schema_site="swagger",
        ),
    )

    return app
