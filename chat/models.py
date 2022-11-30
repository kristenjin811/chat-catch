from pydantic import BaseModel


class TestIn(BaseModel):
    test1: str
    email: str
    name: str
    number: int
