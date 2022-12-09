# from fastapi.testclient import TestClient
# from main import app
# from queries.messages import MessageQueries

# client = TestClient(app)

# TestMessage = {
#     "message": "message",
#     "edited": True
# }


# def test_create_message():
#     class TestMessageQuery:
#         def create_message(self):
#             pass

#     app.dependency_overrides[MessageQueries] = TestMessageQuery
#     response = client.post("/api/messages/", json=TestMessage)
#     assert response.status_code == 200
#     assert response.json() == TestMessage
#     app.dependency_overrides = {}
