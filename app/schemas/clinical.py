from pydantic import BaseModel, conint, constr


class VitalSign(BaseModel):
    heart_rate: conint(ge=0)
    blood_pressure: constr(regex='^\d{2,3}/\d{2,3}$')  # e.g., '120/80'
    temperature: float


class Condition(BaseModel):
    name: constr(min_length=1)
    is_chronic: bool


class HeartFailure(BaseModel):
    ejection_fraction: conint(ge=0, le=100)
    symptoms: list[str]
    condition: Condition


class Treatment(BaseModel):
    name: constr(min_length=1)
    duration_days: conint(ge=1)
    vital_signs: VitalSign


class Score(BaseModel):
    score_value: conint(ge=0)
    date_assessed: str  # YYYY-MM-DD format
    heart_failure: HeartFailure