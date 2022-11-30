
class MessagesIn(BaseModel):
  message: str
  from_time:

class MessagesQueries:
  def get_all_messages(self):
    result = list(db.messages.find())
    for message in result:
      message["id"] = message["_id"]
    return result
