# from fastapi import APIRouter, Depends, Response
# from queries.messages import MessageIn, MessageOut, MessageQueries
# from bson.objectid import ObjectId


# router = APIRouter()


# @router.post("/api/messages/")
# async def create_message(
#     info: MessageIn,
#     messages: MessageQueries = Depends(),
# ):

#     try:
#         messages.create(info)
#     except Exception as e:
#         print(e)
#     return info


# @router.get("/api/messages/")
# def get_all_messages(response: Response, message: MessageQueries = Depends()):
#     response = message.get_all_messages()
#     return response


# @router.get("/api/messages/{id}")
# def get_message(
#     id: str, message: Response, messages: MessageQueries = Depends()
# ):
#     messages = messages.get_message(ObjectId(id))
#     return MessageOut(**messages)


# @router.delete("/api/messages/{id}", response_model=bool)
# async def delete_message(
#     id: str, messages: Response, message: MessageQueries = Depends()
# ) -> bool:
#     message.delete_message(ObjectId(id))
#     return True


# @router.put("/api/messages/{id}")
# async def create_or_update_message(
#     id: str, message: Response, messages: MessageQueries = Depends()
# ):
#     messages = messages.create_or_update_message(ObjectId(id))

#     # messages = messages.create_or_update_message(ObjectId(id))


# @router.websocket("/chat")
# async def chat():
#     pass
