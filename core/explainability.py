# -------------------------------------------------
# Explainable AI Module
# -------------------------------------------------

def explain_credit_score(
    income,
    credit_utilization,
    repayment_history,
    employment_years=None,
    active_loans=0
):
    explanations = []

    if employment_years is None:
        employment_years = 0

    # Income
    if income >= 100000:
        explanations.append("High income contributed positively to your credit score.")
    elif income >= 60000:
        explanations.append("Moderate income added reasonable points to your score.")
    else:
        explanations.append("Low income limited your credit score growth.")

    # Credit utilization
    if credit_utilization < 30:
        explanations.append("Low credit utilization improved your score significantly.")
    elif credit_utilization < 50:
        explanations.append("Moderate credit utilization slightly reduced your score.")
    else:
        explanations.append("High credit utilization negatively impacted your score.")

    # Repayment history
    if repayment_history == "excellent":
        explanations.append("Excellent repayment history strongly improved your score.")
    elif repayment_history == "good":
        explanations.append("Good repayment history had a positive impact.")
    elif repayment_history == "average":
        explanations.append("Average repayment history limited score improvement.")
    else:
        explanations.append("Poor repayment history significantly reduced your score.")

    # Employment stability
    if employment_years >= 5:
        explanations.append("Stable employment history increased your score.")
    elif employment_years >= 2:
        explanations.append("Moderate employment stability added some confidence.")
    else:
        explanations.append("Low employment stability reduced score confidence.")

    # Active loans
    if active_loans == 0:
        explanations.append("No active loans positively affected your score.")
    elif active_loans <= 2:
        explanations.append("Existing loans had a minor negative impact.")
    else:
        explanations.append("Multiple active loans significantly increased risk.")

    return explanations


def explain_risk_decision(rule_risk, ml_risk):
    """
    Explain why the final risk decision was made
    """

    explanations = []

    # Rule-based risk explanation
    if rule_risk == "High Risk":
        explanations.append(
            "Rule-based policy identified high risk due to repayment behavior, utilization, or loan burden."
        )
    elif rule_risk == "Medium Risk":
        explanations.append(
            "Rule-based policy identified moderate risk based on credit score and active loans."
        )
    else:
        explanations.append(
            "Rule-based policy identified low risk with stable financial indicators."
        )

    # ML-based risk explanation
    if ml_risk == "High":
        explanations.append(
            "AI model predicted high default probability based on learned financial patterns."
        )
    elif ml_risk == "Medium":
        explanations.append(
            "AI model predicted moderate risk considering combined financial factors."
        )
    else:
        explanations.append(
            "AI model predicted low risk due to strong financial profile."
        )

    return explanations
