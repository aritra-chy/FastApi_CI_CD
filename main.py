from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    name: str
    description: str

todos: List[Todo] = []
api = FastAPI()

@api.get("/")
def home():
    return {"message": "Hello World"}

@api.get("/todos")
def get_todos():
    return todos

@api.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for t in todos:
        if t.id == todo_id:
            t.name = todo.name
            t.description = todo.description
            return t
    return {"message": "Todo not found"}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for t in todos:
        if t.id == todo_id:
            todos.remove(t)
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}

