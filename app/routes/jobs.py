from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Job
from app.schemas import JobCreate


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


# Database dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# =========================
# CREATE JOB
# =========================

@router.post("/")
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db)
):

    new_job = Job(
        title=job.title,
        company=job.company,
        salary=job.salary
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


# =========================
# READ ALL JOBS
# =========================

@router.get("/")
def get_jobs(
    db: Session = Depends(get_db)
):

    return db.query(Job).all()


# =========================
# READ ONE JOB
# =========================

@router.get("/{job_id}")
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job


# =========================
# UPDATE JOB
# =========================

@router.put("/{job_id}")
def update_job(
    job_id: int,
    job_data: JobCreate,
    db: Session = Depends(get_db)
):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    job.title = job_data.title
    job.company = job_data.company
    job.salary = job_data.salary

    db.commit()
    db.refresh(job)

    return job


# =========================
# DELETE JOB
# =========================

@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    db.delete(job)
    db.commit()

    return {
        "message": "Job deleted successfully"
    }