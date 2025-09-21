from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
api = FastAPI()
class Todo(BaseModel):
    id:int
    name:str
    des:str

todos: List[Todo]=[]
@api.get("/")
def index():
    return {"message": "Hello World"}

@api.get("/todos")
def get_todo():
    return todos

@api.post("/todo")
def add_todo(todo:Todo):
    todos.append(todo)
    return todos

@api.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo:Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return todos
    return {"error": "Todo not found"}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id ==todo_id:
            deleted = todos.pop(index)
            return deleted
    return {"error": "Todo not found"}