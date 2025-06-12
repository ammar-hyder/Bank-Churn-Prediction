# streamlit_app.py
import streamlit as st
import requests

st.title("Churn Prediction App")

st.write("Enter customer data to predict churn:")

# Form for user input
with st.form("churn_form"):
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
    country = st.selectbox("Country", ["France", "Spain", "Germany"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, value=40)
    tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, value=3)
    balance = st.number_input("Balance", min_value=0.0, value=50000.00)
    products_number = st.selectbox("Number of Products", [1, 2, 3, 4])
    credit_card = st.selectbox("Has Credit Card", ["No", "Yes"])
    active_member = st.selectbox("Active Member", ["No", "Yes"])
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=70000.00)

    submit = st.form_submit_button("Predict")

# Map inputs
country_map = {"France": 0, "Spain": 1, "Germany": 2}
gender_map = {"Male": 0, "Female": 1}
credit_card_map = {"No": 0, "Yes": 1}
active_map = {"No": 0, "Yes": 1}

if submit:
    input_data = {
        "credit_score": credit_score,
        "country": country_map[country],
        "gender": gender_map[gender],
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": credit_card_map[credit_card],
        "active_member": active_map[active_member],
        "estimated_salary": estimated_salary
    }

    # Send to Flask API
    response = requests.post("http://localhost:5000/predict", json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Churn: {'Yes' if result['prediction'] == 1 else 'No'}")
    else:
        st.error("Prediction failed. Please try again.")
