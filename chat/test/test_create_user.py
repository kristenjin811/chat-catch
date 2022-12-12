# from dotenv import load_dotenv
# load_dotenv()
# from fastapi.testclient import TestClient # noqa
# from unittest import TestCase # noqa
# from main import app # noqa
# from queries.accounts import AccountQueries # noqa


# client = TestClient(app)


# TestUser = {
#     "email": "user@email.com",
#     "password": "password",
#     "full_name": "full_name",
# }

# TestUserCreated = {
#     "id": "639281736dc1541c96bba8cb",
#     "email": "user@email.com",
#     "full_name": "full_name",
# }


# def test_create_account():
#     class TestUserQuery(TestCase):
#         def create():
#             pass

#     app.dependency_overrides[AccountQueries.create] = (
#         TestUserQuery,

#     )
#     print("Did i get here line 40")
#     response = client.post("/api/accounts", json=TestUser)
#     print(response.json())
#     assert response.status_code == 200
#     assert len(response.json()["account"]["id"]) == len(TestUserCreated["id"])# noqa
#     assert response.json()["account"]["email"] == TestUserCreated["email"]
#     assert (response.json()["account"]["full_name"] == TestUserCreated["full_name"]) # noqa
#     app.dependency_overrides = {}
