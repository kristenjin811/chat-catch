from fastapi.testclient import TestClient
from queries.users import UserQueries
from main import app


client = TestClient(app)


def test_get_all_users():
    class TestQuery:
        def get_all_users(self):
            pass

    app.dependency_overrides[UserQueries] = TestQuery
    response = client.get("/api/users")
    assert response.status_code == 200
    app.dependency_overrides = {}
