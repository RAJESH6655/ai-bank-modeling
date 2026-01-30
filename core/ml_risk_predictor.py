import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ML_DIR = os.path.join(BASE_DIR, "..", "ml")

model = joblib.load(os.path.join(ML_DIR, "risk_model.pkl"))
history_encoder = joblib.load(os.path.join(ML_DIR, "history_encoder.pkl"))
risk_encoder = joblib.load(os.path.join(ML_DIR, "risk_encoder.pkl"))

FEATURE_NAMES = [
    "credit_score",
    "income",
    "credit_utilization",
    "repayment_history",
    "employment_years",
    "active_loans"
]

def predict_ml_risk(
    credit_score,
    income,
    credit_utilization,
    repayment_history,
    employment_years,
    active_loans
):
    encoded_history = history_encoder.transform([repayment_history])[0]

    X = pd.DataFrame([[
        credit_score,
        income,
        credit_utilization,
        encoded_history,
        employment_years,
        active_loans
    ]], columns=FEATURE_NAMES)

    risk_code = model.predict(X)[0]
    return risk_encoder.inverse_transform([risk_code])[0]
