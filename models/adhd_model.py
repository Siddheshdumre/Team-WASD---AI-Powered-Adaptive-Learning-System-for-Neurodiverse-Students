def analyze_adhd_responses(responses):
    """
    Processes ADHD questionnaire responses.
    """
    threshold = 6  # Based on clinical ADHD screening
    score = sum(responses)  # Sum of all responses
    diagnosis = "Positive for ADHD" if score >= threshold else "Negative for ADHD"
    
    return {"score": score, "diagnosis": diagnosis}
