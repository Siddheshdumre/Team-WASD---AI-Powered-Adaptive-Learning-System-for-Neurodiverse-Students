def analyze_learning_speed(time_taken):
    """
    Classifies learning speed based on response time.
    """
    if time_taken < 5:
        return "Fast Learner"
    elif 5 <= time_taken <= 15:
        return "Normal Learner"
    else:
        return "Slow Learner"
