# from dotenv import load_dotenv
# load_dotenv()
# from fastapi.testclient import TestClient
# from unittest import TestCase
# from main import app
# from queries.accounts import AccountQueries


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
#         def create(self, id, email, full_name):
#             return ["639281736dc1541c96bba8cb",
#               "user@email.com",
#               "full_name"]

#         def override_create_account():
#             return {
#                 "id": "63926ec4cd9500b75f3333f3",
#                 "email": "user@email.com",
#                 "full_name": "full_name",
#             }

#     app.dependency_overrides[AccountQueries,
#         AccountQueries.create] = (
#         TestUserQuery,
#         TestUserQuery.override_create_account,
#     )
#     print("Did i get here line 40")
#     response = client.post("/api/accounts", json=TestUser)
#     print(response.json())
#     assert response.status_code == 200
#     assert len(response.json()["account"]["id"]) ==
#       len(TestUserCreated["id"])
#     assert response.json()["account"]["email"] ==
#       TestUserCreated["email"]
#     assert (
#         response.json()["account"]["full_name"] ==
#           TestUserCreated["full_name"]
#     )
#     app.dependency_overrides = {}
