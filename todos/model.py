from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str

    class Config:
        Schema_extra = {
            "example": {
                "item": "item schema",
                "status": "Example schema!"
            }
        }


class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        Schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }
