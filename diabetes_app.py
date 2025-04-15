import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("best_diabetes_model.pkl")

# Define feature names
feature_names = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'Sudden Weight Loss',
                 'Weakness', 'Polyphagia', 'Genital Thrush', 'Visual Blurring',
                 'Itching', 'Irritability', 'Delayed Healing', 'Partial Paresis',
                 'Muscle Stiffness', 'Alopecia', 'Obesity']

def predict_diabetes(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return "Patient Diagnosed with early-stage diabetes" if prediction[0] == 1 else "Individual assessed as low-risk for diabetes "

# Streamlit UI
st.title("Early-Stage Diabetes Prediction")
st.write("Enter the following details to predict the risk of diabetes.")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)
gender = st.radio("Gender", ["Male", "Female"])
polyuria = st.radio("Polyuria (Frequent Urination)", ["Yes", "No"])
polydipsia = st.radio("Polydipsia (Excessive Thirst)", ["Yes", "No"])
sudden_weight_loss = st.radio("Sudden Weight Loss", ["Yes", "No"])
weakness = st.radio("Weakness", ["Yes", "No"])
polyphagia = st.radio("Polyphagia (Excessive Hunger)", ["Yes", "No"])
genital_thrush = st.radio("Genital Thrush", ["Yes", "No"])
visual_blurring = st.radio("Visual Blurring", ["Yes", "No"])
itching = st.radio("Itching", ["Yes", "No"])
irritability = st.radio("Irritability", ["Yes", "No"])
delayed_healing = st.radio("Delayed Healing", ["Yes", "No"])
partial_paresis = st.radio("Partial Paresis", ["Yes", "No"])
muscle_stiffness = st.radio("Muscle Stiffness", ["Yes", "No"])
alopecia = st.radio("Alopecia (Hair Loss)", ["Yes", "No"])
obesity = st.radio("Obesity", ["Yes", "No"])

# Encode Inputs
input_data = [
    age,
    1 if gender == "Male" else 0,
    1 if polyuria == "Yes" else 0,
    1 if polydipsia == "Yes" else 0,
    1 if sudden_weight_loss == "Yes" else 0,
    1 if weakness == "Yes" else 0,
    1 if polyphagia == "Yes" else 0,
    1 if genital_thrush == "Yes" else 0,
    1 if visual_blurring == "Yes" else 0,
    1 if itching == "Yes" else 0,
    1 if irritability == "Yes" else 0,
    1 if delayed_healing == "Yes" else 0,
    1 if partial_paresis == "Yes" else 0,
    1 if muscle_stiffness == "Yes" else 0,
    1 if alopecia == "Yes" else 0,
    1 if obesity == "Yes" else 0,
]

# Predict Button
if st.button("Predict Diabetes"):
    result = predict_diabetes(input_data)
    st.subheader(f"Prediction: {result}")