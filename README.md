# FastAPI + Pydantic — Important Concepts

This README covers three important concepts used in FastAPI projects:

* `model_dump()`
* `app.include_router()`
* `Field()`

---

## 1. `model_dump()`

`model_dump()` is a **Pydantic method** used to convert a Pydantic model into a normal Python dictionary.

### Flow

```text
Pydantic Model
      │
      ▼
 model_dump()
      │
      ▼
Python Dictionary
```

### Example

```python
from pydantic import BaseModel

class Job(BaseModel):
    title: str
    salary: int

job = Job(
    title="Python Developer",
    salary=700000
)

data = job.model_dump()

print(data)
```

### Output

```python
{
    "title": "Python Developer",
    "salary": 700000
}
```

### Why use `model_dump()`?

It is useful when you need to:

* Convert Pydantic data into a dictionary
* Send data to a database
* Process data like a normal Python dictionary
* Prepare data for other operations

### 🧠 Remember

```text
Pydantic Model → model_dump() → Python Dictionary
```

---

# 2. `app.include_router()`

`app.include_router()` is used to **register a router's endpoints with the main FastAPI application**.

Instead of keeping all API routes inside `main.py`, we can separate them into different routers.

### Project Structure

```text
FastAPI Application
│
├── main.py
│
├── routers/
│   ├── jobs.py
│   ├── users.py
│   ├── auth.py
│   └── admin.py
│
└── models/
```

### Router Flow

```text
                    FastAPI App
                        │
                        ▼
               app.include_router()
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
     jobs_router   users_router   auth_router
          │             │             │
          ▼             ▼             ▼
       /jobs/        /users/        /auth/
```

### Example

#### `jobs.py`

```python
from fastapi import APIRouter

jobs_router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@jobs_router.get("/")
def get_jobs():
    return {"message": "All jobs"}
```

#### `main.py`

```python
from fastapi import FastAPI
from routers.jobs import jobs_router

app = FastAPI()

app.include_router(jobs_router)
```

Now the endpoint is available at:

```text
GET /jobs/
```

### Multiple Routers

```python
app.include_router(jobs_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(admin_router)
```

### 🧠 Remember

```text
include_router()
       ↓
Connect Router
       ↓
FastAPI Application
       ↓
Routes become available
```

---

# 3. `Field()`

`Field()` is provided by **Pydantic** and is used to define:

* Validation rules
* Default values
* Constraints
* Metadata
* API documentation information

### Basic Example

```python
from pydantic import BaseModel, Field

class Job(BaseModel):
    title: str = Field(...)
    salary: int = Field(..., gt=0)
    experience: int = Field(default=0, ge=0)
```

---

## Understanding `Field()`

### Required Field

```python
title: str = Field(...)
```

`...` means the field is **required**.

---

### Greater Than

```python
salary: int = Field(..., gt=0)
```

`gt=0` means:

```text
salary > 0
```

---

### Default Value

```python
experience: int = Field(default=0, ge=0)
```

This means:

```text
Default value = 0
ge=0 → greater than or equal to 0
```

---

## Useful `Field()` Options

| Option              | Meaning                           |
| ------------------- | --------------------------------- |
| `...`               | Required field                    |
| `default=0`         | Default value                     |
| `gt=0`              | Greater than 0                    |
| `ge=0`              | Greater than or equal to 0        |
| `lt=100`            | Less than 100                     |
| `le=100`            | Less than or equal to 100         |
| `min_length=3`      | Minimum string length             |
| `max_length=50`     | Maximum string length             |
| `description="..."` | Description for API documentation |

### Example

```python
class Job(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Job title"
    )
```

This means:

```text
Required
   +
Minimum 3 characters
   +
Maximum 50 characters
   +
Description in API documentation
```

---

## Range Validation Example

```python
age: int = Field(
    ...,
    ge=18,
    le=60
)
```

This means:

```text
        age
         │
         ▼
      Required
         │
         ▼
    18 ≤ age ≤ 60
```

---

# 🔥 Complete FastAPI Flow

These concepts can work together in a FastAPI application:

```text
                    CLIENT
                       │
                       ▼
              FastAPI Application
                       │
                       ▼
             app.include_router()
                       │
                       ▼
                 jobs_router
                       │
                       ▼
                  /jobs/
                       │
                       ▼
                Pydantic Model
                       │
                       ▼
                    Field()
                       │
                       ▼
                  Validation
                       │
                       ▼
               Validated Data
                       │
                       ▼
                model_dump()
                       │
                       ▼
               Python Dictionary
                       │
                       ▼
                   Database
```

---

# 🧠 Quick Memory Trick

```text
Field()
    ↓
Validate the data

include_router()
    ↓
Connect the routes

model_dump()
    ↓
Convert Pydantic Model → Dictionary
```

---

# 🎯 Interview Answers

### What is `Field()`?

> `Field()` is used in Pydantic models to define validation rules, default values, constraints, and metadata for individual fields.

### What is `app.include_router()`?

> `app.include_router()` registers the endpoints defined in an `APIRouter` with the main FastAPI application.

### What is `model_dump()`?

> `model_dump()` converts a Pydantic model into a Python dictionary, which is useful for data processing and database operations.

---

## Summary

| Concept            | Main Purpose                             |
| ------------------ | ---------------------------------------- |
| `Field()`          | Validate and configure model fields      |
| `include_router()` | Register and organize API routes         |
| `model_dump()`     | Convert Pydantic model into a dictionary |

### Easy Formula

```text
Field() → Validation
     ↓
Router → API Routes
     ↓
model_dump() → Dictionary
```
