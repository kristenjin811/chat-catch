from fastapi.testclient import TestClient
from main import app
from queries.chatrooms import ChatroomQueries

client = TestClient(app)

async def test_get_chatroom():
    # Create a chatroom in the database
    await insert_chatroom("Alice", "Test Room")

    # Retrieve the chatroom from the database
    chatroom = await get_chatroom("Test Room")

    # Assert that the chatroom was returned
    assert chatroom is not None

    # Assert that the chatroom has the expected name
    assert chatroom["chatroom_name"] == "Test Room"

    # Assert that the chatroom has a member named "Alice"
    assert any(member["username"] == "Alice" for member in chatroom["members"])
