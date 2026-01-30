import sys
import os

# -------------------------------------------------
# Fix Python path for Streamlit
# -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

import streamlit as st

from core.explainability import explain_credit_score, explain_risk_decision
from core.credit_score import generate_credit_score
from core.final_risk_engine import get_final_risk
from core.bank_recommender import recommend_banks

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(page_title="AI Bank Modeling", page_icon="🏦", layout="centered")

st.title("🏦 AI Bank Modeling")
st.write("Real-world AI Credit Scoring & Smart Bank Recommendation System")

st.divider()

# -------------------------------------------------
# User Inputs
# -------------------------------------------------
st.header("📋 Enter Your Financial Details")

income = st.number_input(
    "Monthly Income (₹)",
    min_value=10000,
    max_value=1000000,
    step=5000
)

credit_utilization = st.slider(
    "Credit Card Utilization (%)",
    min_value=0,
    max_value=100,
    value=30
)

repayment_history = st.selectbox(
    "Repayment History",
    ["excellent", "good", "average", "poor"]
)

employment_years = st.number_input(
    "Employment Stability (Years)",
    min_value=0,
    max_value=40
)

active_loans = st.number_input(
    "Number of Active Loans",
    min_value=0,
    max_value=19
)

st.divider()

# -------------------------------------------------
# Processing
# -------------------------------------------------
if st.button("🔍 Analyze Credit Profile"):

    annual_income = income * 12

    # -------- Credit Score --------
    credit_score = generate_credit_score(
        income=annual_income,
        credit_utilization=credit_utilization,
        repayment_history=repayment_history,
        employment_years=employment_years,
        active_loans=active_loans
    )

    # -------- Hybrid Risk Engine --------
    rule_risk, ml_risk, final_risk = get_final_risk(
        credit_score=credit_score,
        income=annual_income,
        credit_utilization=credit_utilization,
        repayment_history=repayment_history,
        employment_years=employment_years,
        active_loans=active_loans
    )

    # -------- Bank Recommendation --------
    score_category, banks = recommend_banks(credit_score)
    
    # -------------------------------------------------
    # Explainable AI Section
    # -------------------------------------------------
    st.divider()
    st.subheader("🧠 AI Explanation (Why this decision?)")

    st.markdown("### 📊 Credit Score Explanation")
    score_explanations = explain_credit_score(
        income=annual_income,
        credit_utilization=credit_utilization,
        repayment_history=repayment_history,
        active_loans=active_loans
    )

    for exp in score_explanations:
        st.write("•", exp)

    st.markdown("### ⚠ Risk Decision Explanation")
    risk_explanations = explain_risk_decision(rule_risk, ml_risk)

    for exp in risk_explanations:
        st.write("•", exp)

    # -------------------------------------------------
    # Output Section
    # -------------------------------------------------
    st.success("✅ Credit Profile Generated Successfully")

    col1, col2 = st.columns(2)
    col1.metric("📊 Credit Score", credit_score)
    col2.metric("⚠ Final Risk Category", final_risk)

    st.write(" **Rule-based Risk:**", rule_risk)

    st.divider()

    st.metric("📊 Credit Score Category", score_category)
    if banks:
        for bank in banks:
            st.write(f"✔ {bank}")
    else:
        st.warning("No suitable banks found for this profile.")

    st.divider()

    # -------------------------------------------------
    # Improvement Suggestions
    # -------------------------------------------------
    st.subheader("💡 Suggestions to Improve Eligibility")

    if credit_utilization > 50:
        st.write("• Reduce credit card utilization below 30%")
    if repayment_history in ["average", "poor"]:
        st.write("• Maintain timely repayments for 3–6 months")
    if active_loans > 5:
        st.write("• Avoid taking new loans temporarily")
    if employment_years < 1.5:
        st.write("• Improve employment stability")
    if credit_score >= 750:
        st.write("• Excellent profile.")
