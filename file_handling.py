import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mock prediction function
def predict_approval(income, credit_score, loan_amount):
    # Fake logic for demo purposes
    score = (income / loan_amount) + (credit_score / 850)
    return "Approved" if score > 1.2 else "Rejected"

# App Title
st.title("🏦 Loan Approval Predictor")

# Sidebar inputs
st.sidebar.header("Applicant Details")
income = st.sidebar.slider("Monthly Income ($)", 1000, 20000, 5000)
credit_score = st.sidebar.slider("Credit Score", 300, 850, 650)
loan_amount = st.sidebar.number_input("Loan Amount ($)", min_value=500, max_value=50000, value=10000)

# Display input summary
st.subheader("📊 Applicant Summary")
st.write(f"**Income:** ${income}")
st.write(f"**Credit Score:** {credit_score}")
st.write(f"**Loan Amount:** ${loan_amount}")

# Prediction
st.subheader("✅ Prediction Result")
result = predict_approval(income, credit_score, loan_amount)
st.success(f"Your loan is likely to be **{result}**.")

# Visualization
st.subheader("📉 Financial Breakdown")
fig, ax = plt.subplots()
labels = ['Income', 'Loan Amount']
values = [income, loan_amount]
ax.bar(labels, values, color=['green', 'red'])
st.pyplot(fig)

# DataFrame display
st.subheader("📋 Applicant Data")
df = pd.DataFrame({
    "Income": [income],
    "Credit Score": [credit_score],
    "Loan Amount": [loan_amount],
    "Prediction": [result]
})
st.dataframe(df)
