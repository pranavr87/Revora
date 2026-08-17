from io import BytesIO

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.schemas.diagnosis import DiagnosisRequest

from app.services.vehicle_service import (
    fetch_brands,
    fetch_models,
    fetch_symptoms,
    fetch_diagnosis,
    fetch_multiple_diagnosis,
    fetch_search_results,
    fetch_pdf_report,
)

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)


class PDFRequest(BaseModel):

    brand: str

    model: str

    symptom: str


@router.get("/brands")
def get_brands():

    return {

        "brands": fetch_brands()

    }


@router.get("/models/{brand}")
def get_models(brand: str):

    return {

        "models": fetch_models(brand)

    }


@router.get("/symptoms")
def get_symptoms():

    return {

        "symptoms": fetch_symptoms()

    }


@router.get("/diagnose/{symptom}")
def diagnose(symptom: str):

    return fetch_diagnosis(symptom)


@router.post("/diagnose")
def diagnose_vehicle(request: DiagnosisRequest):

    return fetch_diagnosis(request.symptom)


@router.post("/diagnose/multiple")
def diagnose_multiple(request: DiagnosisRequest):

    return fetch_multiple_diagnosis(request.symptom)


@router.get("/search/{keyword}")
def search(keyword: str):

    return {

        "results": fetch_search_results(keyword)

    }


@router.post("/report")
def download_report(request: PDFRequest):

    pdf = fetch_pdf_report(

        request.brand,
        request.model,
        request.symptom

    )

    if pdf is None:

        return {

            "message": "Diagnosis not found."

        }

    return StreamingResponse(

        BytesIO(pdf),

        media_type="application/pdf",

        headers={

            "Content-Disposition":
            "attachment; filename=REVORA_Report.pdf"

        }

    )