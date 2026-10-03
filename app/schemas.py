from pydantic import BaseModel, Field
class JobCreate(BaseModel):
    title:str
    company:str
    salary:int
    
class jobResponse(BaseModel):
    title:str
    company:str
    salary:int
    
