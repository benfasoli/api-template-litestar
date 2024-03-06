from litestar.status_codes import HTTP_200_OK
from litestar.testing import TestClient

from src.app import init_app


def test_get_index() -> None:
    app = init_app()
    with TestClient(app=app) as client:
        response = client.get("/")

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "🚀"}
