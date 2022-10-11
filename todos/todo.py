from fastapi import APIRouter, Path

from model import Todo

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo add successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todo": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo with supplied ID doesn't exist."}


@todo_router.put("/todo/{todo_id}")
async def update_single_todo(todo_data: Todo, todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo = todo_data
            return {"todo": todo}
    return {"message": "Todo with supplied ID doesn't exist."}


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo_id == todo.id:
            todo_list.pop(index)
            return {"message": "Delete todo successfully!"}
    return {"message": "Todo with supplied ID doesn't exist."}


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message": "Todos deleted successfully."}
