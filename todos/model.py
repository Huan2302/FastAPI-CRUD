from pydantic import BaseModel
from typing import List


class TodoItem(BaseModel):
    id: int
    item: str

    class Config:
        Schema_extra = {
            "example": {
                "id": 1,
                "item": "item schema"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        Schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"}
                ]
            }
        }
