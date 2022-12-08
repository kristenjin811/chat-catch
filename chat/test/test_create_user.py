# from fastapi.testclient import TestClient
# from unittest.mock import MagicMock
# from jwtdown_fastapi.authentication import Authenticator
# from authenticator import MyAuthenticator
# from main import app
# from queries.accounts import AccountQueries, AccountOutWithPassword
# import os

# client = TestClient(app)

# TestUser = {
#     "email": "user@email.com",
#     "password": "password",
#     "full_name": "full_name"
# }

# # TestUserCreated = {
# #     "created": True
# # }


# def test_create_account():
#     class TestUserQuery(MyAuthenticator):
#         os_environ_mock = MagicMock()
#         os_environ_mock.__getitem__.return_value = "my_signing_key"
#         Authenticator.os.environ = os_environ_mock

#         def create_account(self):
#             pass

#     app.dependency_overrides[ AccountQueries,] = TestUserQuery
#     response = client.post("/api/accounts/", json=TestUser)
#     assert response.status_code == 200
#     assert response.json.loads() == AccountOutWithPassword
#     app.dependency_overrides = {}
