from fastapi import FastAPI
from app.database import Base,engine
from app import models
from app.routes.jobs import router as jobs_router

Base.metadata.create_all(bind=engine)
app=FastAPI(
    title="Job Portal API",
    description="This is a Job Portal API built with FastAPI",
    version="1.0.0"
)
app.include_router(jobs_router)


@app.get("/")
def home():
    return {"message": "Welcome to the Job Portal API!"}

@app.get("/about")
def about():
    return{
        "Project": "Job Portal API",
        "Developer": "UJJWAL KUMAR",
    }