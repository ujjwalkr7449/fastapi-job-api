from fastapi import APIRouter
from app.schemas import JobCreate

router =APIRouter(
    prefix="/jobs",
    tags=["jobs"]
    
)

jobs=[]
@router.get("/")
def get_jobs():
    return jobs


@router.post("/")
def create_job(job:JobCreate):
    jobs.append(job.Model_dump())
    return {
        "message": "Job created successfully",
        "job": job
    }
    
    
