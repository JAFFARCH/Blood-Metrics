from fastapi import FastAPI, HTTPException
from models.patient_data import PatientData
from services.insights_handler import handle_conversation

app = FastAPI()

@app.post("/api/insights")
async def get_insights(patient_data: PatientData):
    try:
        insights = handle_conversation(patient_data.data)
        return {"insights": insights}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
