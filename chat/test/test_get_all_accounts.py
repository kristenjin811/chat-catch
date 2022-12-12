from fastapi.testclient import TestClient
from queries.accounts import AccountQueries
from main import app


client = TestClient(app)


def test_get_all_accounts():
    class fakegetallaccsQuery:
        def fetch_all_accounts(self):
            return []

    app.dependency_overrides[AccountQueries] = fakegetallaccsQuery
    response = client.get("/api/accounts")
    assert response.status_code == 200
    app.dependency_overrides = {"accounts": []}
