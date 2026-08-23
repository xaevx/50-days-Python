# FastAPI REST API

A simple **REST API** built with Python and FastAPI that provides CRUD operations for managing tasks.

The project demonstrates how Python can be used to create a backend API that can communicate with web applications, mobile applications, and other services.

## Features

- REST API development
- Create tasks
- Read tasks
- Read individual tasks
- Update tasks
- Delete tasks
- JSON responses
- Request validation
- HTTP error handling
- Interactive API documentation
- Automatic API schema generation

## Requirements

Install FastAPI and Uvicorn:

```bash
python -m pip install fastapi uvicorn
```

## Run the Project

Start the FastAPI server:

```bash
uvicorn FastAPI_REST_API:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use this page to test the API endpoints directly from your browser.

## API Endpoints

### Home

```text
GET /
```

Returns information about the API.

Example response:

```json
{
    "message": "Welcome to the Task Management API",
    "status": "running"
}
```

### Get All Tasks

```text
GET /tasks
```

Returns all tasks.

### Get One Task

```text
GET /tasks/{task_id}
```

Example:

```text
GET /tasks/1
```

Returns the task with ID `1`.

### Create Task

```text
POST /tasks
```

Example request:

```json
{
    "title": "Learn FastAPI",
    "description": "Build a REST API using Python",
    "completed": false
}
```

### Update Task

```text
PUT /tasks/{task_id}
```

Example:

```text
PUT /tasks/1
```

Request:

```json
{
    "title": "Learn FastAPI",
    "description": "Build and test a REST API",
    "completed": true
}
```

### Delete Task

```text
DELETE /tasks/{task_id}
```

Example:

```text
DELETE /tasks/1
```

## CRUD Operations

The API follows the basic CRUD pattern:

```text
Create
  ↓
POST /tasks

Read
  ↓
GET /tasks

Update
  ↓
PUT /tasks/{id}

Delete
  ↓
DELETE /tasks/{id}
```

## How It Works

```text
Client
   ↓
HTTP Request
   ↓
FastAPI
   ↓
Route / Endpoint
   ↓
Request Validation
   ↓
Python Logic
   ↓
JSON Response
   ↓
Client
```

## Data Model

Tasks use the following structure:

```json
{
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Build a REST API",
    "completed": false
}
```

The request model is created using **Pydantic**.

```python
class Task(BaseModel):

    title: str
    description: str
    completed: bool = False
```

## HTTP Methods Used

| Method  | Purpose               |
|---------|-----------------------|
| GET     | Retrieve data         |
| POST    | Create data           |
| PUT     | Update data           |
| DELETE  | Delete data           |

## Error Handling

If a requested task does not exist, the API returns a `404` response.

Example:

```json
{
    "detail": "Task not found"
}
```

## JSON

REST APIs commonly exchange data using **JSON**.

Example:

```json
{
    "title": "Learn Python",
    "description": "Practice FastAPI",
    "completed": false
}
```

## Modules Used

- Python 3
- FastAPI
- Uvicorn
- Pydantic

## What i learned

- REST APIs
- FastAPI
- HTTP Methods
- API Endpoints
- CRUD Operations
- JSON
- Request Validation
- Pydantic Models
- HTTP Status Codes
- Exception Handling
- Uvicorn
- API Documentation

---

⭐ Part of my **#50DaysOfPython** challenge.