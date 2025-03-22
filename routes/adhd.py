from fastapi import APIRouter
from pydantic import BaseModel
from models.adhd_model import analyze_adhd_responses

router = APIRouter()

# Define Request Model
class ADHDTestRequest(BaseModel):
    responses: list[int]

@router.post("/test")
async def adhd_test(request: ADHDTestRequest):
    """
    Receives user's ADHD test responses and provides analysis.
    """
    result = analyze_adhd_responses(request.responses)
    return {"ADHD Score": result["score"], "Likely ADHD": result["diagnosis"]}
