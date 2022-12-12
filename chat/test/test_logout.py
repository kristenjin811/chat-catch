from fastapi.testclient import TestClient
from main import app

fakeToken = "asdfghjk12442477888889998666"


def test_logout():
    with TestClient(app) as client:
        response = client.delete("/token")
        assert response.status_code == 200
        assert response.json() is True
