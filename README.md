# fastapi-job-api
# model_dump(): 

model_dump() is a Pydantic method used to convert a Pydantic model/object into a normal Python dictionary.

Pydantic Model
      ↓
 model_dump()
      ↓
Python Dictionary"""



# include_router:
"""Hey, include all the routes from jobs_router in my application.main.py
Registers a router's endpoints with the main FastAPI application.
   │
   ├── jobs_router
   ├── users_router
   ├── auth_router
   └── admin_router
app.include_router(jobs_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(admin_router) """


# Field : 
"""Basic example
from pydantic import BaseModel, Field

class Job(BaseModel):
    title: str = Field(...)
    salary: int = Field(..., gt=0)
    experience: int = Field(default=0, ge=0)
    
What does each mean?
title: str = Field(...)

... means required.

salary: int = Field(..., gt=0)

Salary must be greater than 0.

experience: int = Field(default=0, ge=0)
Default value = 0
ge=0 → greater than or equal to 0
Other useful options


class Job(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Job title"
    )

This means:

Required
Minimum 3 characters
Maximum 50 characters
Adds description to Swagger docs



Easy way to remember 🧠
Field()
  ↓
Validation + Constraints + Metadata

For example:

age: int = Field(..., ge=18, le=60)

means:

age is required and must be between 18 and 60.

Interview answer:

"Field() is used in Pydantic models to define validation rules, default values, constraints, and metadata for individual fields."""