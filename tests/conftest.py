"""
Global pytest configuration.
"""

import litestar
import pytest

from src import bootstrap


@pytest.fixture
def app() -> litestar.Litestar:
    postgres_uri = "postgres://postgres:postgres@localhost:5432/postgres"
    log_level = "DEBUG"
    app = bootstrap.create_app(
        postgres_uri=postgres_uri,
        log_level=log_level,
    )
    return app
