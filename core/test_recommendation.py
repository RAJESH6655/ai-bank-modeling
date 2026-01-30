from credit_score import generate_credit_score
from risk_classifier import classify_risk
from bank_recommender import recommend_banks

credit_score = generate_credit_score(
    income=75000,
    credit_utilization=35,
    repayment_history="good",
    employment_years=5,
    active_loans=1
)

risk = classify_risk(
    credit_score=credit_score,
    income=75000,
    credit_utilization=35,
    repayment_history="good",
    active_loans=1
)

banks = recommend_banks(
    credit_score=credit_score,
    income=75000,
    risk_category=risk
)

print("Credit Score:", credit_score)
print("Risk Category:", risk)
print("Recommended Banks:")
for bank in banks:
    print("-", bank)
