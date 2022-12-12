# from fastapi.testclient import TestClient
# from main import app
# from api.users import

# from api.chatrooms import ChatroomQueries
# from controllers.chatrooms import insert_chatroom, get_chatroom

# # client = TestClient(app)


# async def test_get_chatroom():
#     # Create a chatroom in the database
#     await insert_chatroom("Alice", "Test Room")

#     # Retrieve the chatroom from the database
#     chatroom = await get_chatroom("Test Room")

#     # Assert that the chatroom was returned
#     assert chatroom is not None

#     # Assert that the chatroom has the expected name
#     assert chatroom["chatroom_name"] == "Test Room"

#     # Assert that the chatroom has a member named "Alice"
#     assert any(member["username"] ==
#       "Alice" for member in chatroom["members"])


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
