import litestar
import pytest


@pytest.fixture
def app() -> litestar.Litestar:
    from src import bootstrap, environment

    app = bootstrap.create_app(
        postgres_uri=environment.POSTGRES_URI,
        log_level=environment.LOG_LEVEL,
    )

    return app
