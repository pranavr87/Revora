from pydantic import BaseModel

class DiagnosisRequest(BaseModel):
    brand: str
    model: str
    symptom: str