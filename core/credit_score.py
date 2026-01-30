def generate_credit_score(
    income,
    credit_utilization,
    repayment_history,
    employment_years,
    active_loans
):
    """
    Generate AI-based credit score (300–900)
    """

    score = 300  # base score

    # Income factor (0–200)
    if income > 100000:
        score += 200
    elif income > 60000:
        score += 150
    elif income > 30000:
        score += 100
    else:
        score += 50

    # Credit utilization (0–250)
    # Ideal utilization < 30%
    if credit_utilization < 30:
        score += 250
    elif credit_utilization < 50:
        score += 180
    else:
        score += 80

    # Repayment history (0–200)
    if repayment_history == "excellent":
        score += 200
    elif repayment_history == "good":
        score += 150
    elif repayment_history == "average":
        score += 80
    else:
        score += 30

    # Employment stability (0–100)
    score += min(employment_years * 20, 100)

    # Active loans penalty
    score -= active_loans * 30

    # Bound score
    score = max(300, min(score, 900))

    return score
