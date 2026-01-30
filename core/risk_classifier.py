def classify_risk(
    credit_score,
    credit_utilization,
    repayment_history,
    active_loans
):
    """
    Classify customer risk into Low / Medium / High
    """

    # High risk conditions
    if (
        credit_score < 550
        or repayment_history == "poor"
        or credit_utilization > 75
    ):
        return "High Risk"

    # Medium risk conditions
    if (
        credit_score < 700
        or active_loans >= 3
        or credit_utilization > 50
    ):
        return "Medium Risk"

    # Otherwise
    return "Low Risk"
