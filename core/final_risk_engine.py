from core.risk_classifier import classify_risk
from core.ml_risk_predictor import predict_ml_risk

def get_final_risk(
    credit_score,
    income,
    credit_utilization,
    repayment_history,
    employment_years,
    active_loans
):
    """
    Hybrid Risk Engine:
    Combines rule-based risk and ML-based risk
    """

    # Rule-based risk (policy)
    rule_risk = classify_risk(
        credit_score,
        credit_utilization,
        repayment_history,
        active_loans
    )

    # ML-based risk (prediction)
    ml_risk = predict_ml_risk(
        credit_score,
        income,
        credit_utilization,
        repayment_history,
        employment_years,
        active_loans
    )

    # Escalation logic (bank-style)
    if "High" in (rule_risk, ml_risk):
        final_risk = "High Risk"
    elif "Medium" in (rule_risk, ml_risk):
        final_risk = "Medium Risk"
    else:
        final_risk = "Low Risk"

    return rule_risk, ml_risk, final_risk
