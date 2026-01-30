from credit_score import generate_credit_score

score = generate_credit_score(
    income=75000,
    credit_utilization=35,
    repayment_history="good",
    employment_years=5,
    active_loans=1
)

print("Generated Credit Score:", score)
