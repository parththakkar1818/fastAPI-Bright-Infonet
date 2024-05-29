from pydantic import BaseModel

class Marks(BaseModel):
    maths: int
    science: int


class User(BaseModel):
    name: str
    rollNumber: int
    standard: int
    marks: Marks