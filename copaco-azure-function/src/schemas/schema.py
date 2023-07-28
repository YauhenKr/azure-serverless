from pydantic import BaseModel


class Quote(BaseModel):
    id: str
    content: str
    author: str
