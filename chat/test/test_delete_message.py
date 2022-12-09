# from fastapi.testclient import TestClient
# from main import app
# from queries.messages import MessageQueries


# client = TestClient(app)


# def test_delete_message():
#     class TestDeleteQuery:
#         def delete_message(self, id):
#             pass

#     app.dependency_overrides[MessageQueries] = TestDeleteQuery
#     response = client.delete("/api/messages/63869900562445c3821e465b")
#     assert response.status_code == 200
#     assert response.json() is True
#     app.dependency_overrides = {}
