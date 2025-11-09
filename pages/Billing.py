import streamlit as st
import pandas as pd

# import everything from your model file
from bill_model import predict_bill

st.title("Healthcare Billing Prediction")

st.subheader("Enter Patient Details")

age = st.number_input("Age", min_value=0, max_value=120, value=30)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])

blood_type = st.selectbox(
    "Blood Type",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)

medical_condition = st.selectbox("Medical Condition", 
    ["Diabetes", "Asthma", "Cancer", "Obesity", "Heart Disease", "Other"])

admission_type = st.selectbox(
    "Admission Type",
    ["Emergency", "Urgent", "Elective"]
)

insurance_provider = st.selectbox("Insurance Provider", 
    ["Private", "Government", "Blue Cross", "Aetna", "UnitedHealthcare", "None"])

admission_date = st.date_input("Admission Date")
discharge_date = st.date_input("Discharge Date")

if st.button("Predict Final Bill"):
    bill = predict_bill(
        age=age,
        gender=gender,
        blood_type=blood_type,
        medical_condition=medical_condition,
        admission_type=admission_type,
        insurance_provider=insurance_provider,
        admission_date=str(admission_date),
        discharge_date=str(discharge_date)
    )

    st.success(f"Estimated Final Bill: ${bill:,.2f}")
