import litestar
from litestar.status_codes import HTTP_200_OK
from litestar.testing import TestClient


def test_get_health(app: litestar.Litestar) -> None:
    with TestClient(app=app) as client:
        response = client.get("/health")

    assert response.status_code == HTTP_200_OK, response.text
    assert response.json() is None
