from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model
model = pickle.load(open("salary_api.pkl", "rb"))

# Input Schema
class InputData(BaseModel):
    experience: float

# Home Route
@app.get("/")
def home():
    return {"message": "All OK"}

# Prediction Route
@app.post("/predict")
def predict(data: InputData):

    result = model.predict([[data.experience]])

    return {
        "experience": data.experience,
        "predicted_salary": float(result[0])
    }