# from fastapi.testclient import TestClient
# from main import app
# from queries.users import UserQueries

# client = TestClient(app)

# TestUser = {
#     "username": "username",
#     "email": "user@email.com",
#     "password": "password",
#     "first_name": "string",
#     "last_name": "string",
# }

# TestUserCreated = {
#     "created": True
# }


# def test_create_account():
#     class TestUserQuery:
#         def create_account(self):
#             pass

#     app.dependency_overrides[UserQueries] = TestUserQuery
#     response = client.post("/api/users/", json=TestUser)
#     assert response.status_code == 200
#     assert response.json() == TestUserCreated
#     app.dependency_overrides = {}
