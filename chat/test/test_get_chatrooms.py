# api path for getting all chatrooms
# api.chatrooms passed in MongoClient = Depends(get_nosql_db)
# variable = await get_chatrooms()
#   controllers.get_chatrooms
#   client = await get_nosql_db()
# db = client[MONGODB_DB_NAME]
# collection = db.chatrooms
# rows = collection.find()
# row_list = []
# for row in rows:
#     f_row = format_ids(row)
#     row_list.append(f_row)
# return row_list
#
#
# return chatrooms
client = TestClient(app)

def test_get_chatrooms():
    class TestChatroomQuery:
        def get_all_chatrooms(self):
            return [""]

        def override_get_all_chatrooms():
            return {""}

    app.dependency_overrides[get_chatrooms, get_all_chatrooms] = (TestChatroomQuery, TestChatroomQuery.override_get_all_chatrooms())
    print("before response")
    response = client.get("/api/chatrooms")
    print("response")
    assert response.status_code == 200
    assert len()
