from fastapi import APIRouter
from models.learning_speed_model import analyze_learning_speed

router = APIRouter()

@router.post("/test")
async def learning_speed_test(time_taken: float):
    """
    Determines if the user has a slow, normal, or fast learning speed.
    """
    result = analyze_learning_speed(time_taken)
    return {"Learning Speed": result}
