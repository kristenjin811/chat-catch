from main import app
from controllers.chatrooms import ChatroomQueries
import pytest
from httpx import AsyncClient


class EmptyChatroomQueries:
    async def get_chatrooms(self):
        return []


@pytest.mark.anyio
async def test_get_all_chatrooms():
    app.dependency_overrides[ChatroomQueries] = EmptyChatroomQueries
    async with AsyncClient(
        app=app, base_url=`https://{process.env.REACT_APP_CHAT_API_HOST}/api`
    ) as ac:
        response = await ac.get("/chatrooms")
    assert response.status_code == 200
    assert response.json() == []
    app.dependency_overrides = {}
