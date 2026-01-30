import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Ensure save directory exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------
# Simulated realistic training data
# -----------------------------
data = {
    "credit_score": [820, 760, 720, 680, 640, 600, 560, 520],
    "income": [900000, 850000, 700000, 600000, 500000, 400000, 300000, 250000],
    "credit_utilization": [20, 25, 35, 45, 55, 65, 75, 85],
    "repayment_history": [
        "excellent", "excellent", "good", "good",
        "average", "average", "poor", "poor"
    ],
    "employment_years": [10, 8, 6, 5, 4, 3, 2, 1],
    "active_loans": [0, 1, 1, 2, 2, 3, 4, 5],
    "risk": [
        "Low", "Low", "Low", "Medium",
        "Medium", "Medium", "High", "High"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Encode categorical values
# -----------------------------
history_encoder = LabelEncoder()
risk_encoder = LabelEncoder()

df["repayment_history"] = history_encoder.fit_transform(df["repayment_history"])
df["risk"] = risk_encoder.fit_transform(df["risk"])

X = df.drop("risk", axis=1)
y = df["risk"]

# -----------------------------
# Train model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y)

# -----------------------------
# Save model & encoders
# -----------------------------
joblib.dump(model, os.path.join(BASE_DIR, "risk_model.pkl"))
joblib.dump(history_encoder, os.path.join(BASE_DIR, "history_encoder.pkl"))
joblib.dump(risk_encoder, os.path.join(BASE_DIR, "risk_encoder.pkl"))

print("✅ ML Risk Model trained and saved successfully")
