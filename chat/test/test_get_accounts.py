# from main import app
# from fastapi.testclient import TestClient
# from queries.accounts import AccountOut, AccountQueries


# get_all_accounts = AccountOut(
#   full_name = "admin",
#   email = "admin@gmail.com",
#   id = "63950cbb22b05ec0b760fa2d",
# )
# get_accounts_list = [get_all_accounts]

# class FakeGetAllAccounts:
#   def get_all_accounts(self):
#     return get_accounts_list

# class FakeAccountData:
#   def get_current_account_data(self):
#     return {}

# client = TestClient(app)

# def test_get_accounts_is_protected():
#     app.dependency_overrides[AccountQueries] = FakeGetAllAccounts
#     response = client.get("/api/accounts")
#     assert response.status_code == 200
#     app.dependency_overrides = {}
#     # assert response.json() == get_accounts_list
