from fastapi.testclient import TestClient
from main import app
from queries.accounts import  AccountQueries, AccountOutWithPassword

client = TestClient(app)

TestUser = {
    "email": "user@email.com",
    "password": "password",
    "full_name": "full_name"
}

# TestUserCreated = {
#     "created": True
# }


def test_create_account():
    class TestUserQuery:
        def create_account(self):
            pass

    app.dependency_overrides[ AccountQueries,] = TestUserQuery
    response = client.post("/api/accounts/", json=TestUser)
    assert response.status_code == 200
    assert response.json() == AccountOutWithPassword
    app.dependency_overrides = {}
