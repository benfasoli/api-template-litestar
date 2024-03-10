import litestar
from litestar.status_codes import HTTP_200_OK
from litestar.testing import TestClient


def test_get_index(app: litestar.Litestar) -> None:
    with TestClient(app=app) as client:
        response = client.get("/")

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "🚀"}
