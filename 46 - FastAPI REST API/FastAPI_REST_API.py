from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task Management API",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)

class Task(BaseModel):

    title: str
    description: str
    completed: bool = False

tasks = []

next_id = 1

@app.get("/")
def home():

    return {
        "message": "Welcome to the Task Management API",
        "status": "running"
    }

@app.get("/tasks")
def get_tasks():

    return {"tasks": tasks}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.post("/tasks")
def create_task(task: Task):

    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)
    next_id += 1

    return {
        "message": "Task created successfully",
        "task": new_task
    }

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed

            return {
                "message": "Task updated successfully",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):    
        if task["id"] == task_id:
            deleted_task = tasks.pop(index)

            return {
                "message": "Task deleted successfully",
                "task": deleted_task
            }

    raise HTTPException(status_code=404,detail="Task not found")