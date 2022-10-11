from fastapi import FastAPI
from fastapi import APIRouter
from todo import todo_router

app = FastAPI()
router = APIRouter()


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }


@router.get("/hello")
async def hello() -> dict:
    return {
        "message": "Hello world"
    }

app.include_router(todo_router)
