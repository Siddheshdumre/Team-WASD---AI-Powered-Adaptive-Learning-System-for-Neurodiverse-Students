from fastapi import APIRouter, HTTPException
from models.dyslexia_model import process_dyslexia_test

router = APIRouter()

@router.post("/test")
async def dyslexia_test(payload: dict):
    """
    Endpoint for dyslexia screening test.
    Expects a JSON payload with:
      - user_text: The sentence input by the user.
      - random_sentence: The original sentence presented.
    """
    user_text = payload.get("user_text")
    random_sentence = payload.get("random_sentence")
    
    if not user_text or not random_sentence:
        raise HTTPException(status_code=400, detail="Both user_text and random_sentence are required.")
    
    result = process_dyslexia_test(user_text, random_sentence)
    return {"Dyslexia Score": result["score"], "Diagnosis": result["diagnosis"]}
