from pydantic import BaseModel
from datetime import date

class PatientCreate(BaseModel):
    name: str
    sex: str
    birth_date: date

class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True

class PatientWithVisits(PatientResponse):
    visits: list = []

    class Config:
        from_attributes = True