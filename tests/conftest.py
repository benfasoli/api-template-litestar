"""
Global pytest configuration.
"""

import litestar
import pytest
from dotenv import load_dotenv

load_dotenv(".env.local")


@pytest.fixture
def app() -> litestar.Litestar:
    from src.app import app

    return app
