from fastapi import APIRouter
router =APIRouter(
    prefix="/jobs",
    tags=["jobs"]
    
)

jobs=[]
@router.get("/")
def get_jobs():
    return jobs


@router.post("/")
def create_job(job:dict):
    jobs.append(job)
    return {
        "message": "Job created successfully",
        "job": job
    }
    