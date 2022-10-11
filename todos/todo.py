from fastapi import APIRouter, Path, HTTPException, status

from model import TodoItems, TodoItem

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo", status_code=201)
async def add_todo(todo: TodoItem) -> dict:
    todo_list.append(todo)
    return {"message": "Todo add successfully"}


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@todo_router.put("/todo/{todo_id}")
async def update_single_todo(todo_data: TodoItem,
                             todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
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
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message": "Todos deleted successfully."}
