import streamlit as st
import requests

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title(" Customer Churn Prediction App")
st.markdown("Fill in the customer details below to predict churn probability.")

# Input fields
credit_score = st.number_input("Credit Score", min_value=1)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1)
tenure = st.number_input("Tenure (years)", min_value=0)
balance = st.number_input("Account Balance", min_value=0.0)
num_products = st.number_input("Number of Products", min_value=1)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0)

# Submit button
if st.button("Predict Churn"):
    payload = {
        "CreditScore": credit_score,
        "Geography": geography,
        "Gender": gender,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": has_cr_card,
        "IsActiveMember": is_active,
        "EstimatedSalary": estimated_salary
    }

    try:
        response = requests.post("https://customer-churn-predictor-n61k.onrender.com/predict", json=payload)
        result = response.json()

        if "error" in result:
           st.error(f"Prediction failed: {result['error']}")
        elif "churn_prediction" in result:
           st.success(f"Churn Prediction: {'Yes' if result['churn_prediction'] else 'No'}")
           st.metric("Churn Probability", f"{result['churn_probability']:.2%}") 
        else:
           st.error("Unexpected response format.")

    except Exception as e:
        st.error(f"Connection error: {e}")
