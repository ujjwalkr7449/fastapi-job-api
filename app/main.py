from fastapi import FastAPI
app=FastAPI(
    title="Job Portal API",
    description="This is a Job Portal API built with FastAPI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to the Job Portal API!"}

@app.get("/about")
def about():
    return{
        "Project": "Job Portal API",
        "Developer": "UJJWAL KUMAR",
    }