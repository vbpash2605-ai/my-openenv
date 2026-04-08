from pydantic import BaseModel

class Observation(BaseModel):
    task: str
    content: str

class Action(BaseModel):
    response: str
