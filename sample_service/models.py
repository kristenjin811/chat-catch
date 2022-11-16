from pydantic import BaseModel, Field
import uuid

# Model to append a emoji/picture_url to a message

class Reaction(BaseModel):
    picture_url: str = Field(...)

    class Config:
        schema_extra = {"example":{"picture_url": "picture.com"}}
