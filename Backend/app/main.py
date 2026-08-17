from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.vehicles import router as vehicle_router

app = FastAPI(
    title="Vehicle Fault Detection API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "https://revora-1.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vehicle_router)


@app.get("/")
def home():
    return {
        "message": "🚗 Vehicle Fault Detection API is Running!"
    }