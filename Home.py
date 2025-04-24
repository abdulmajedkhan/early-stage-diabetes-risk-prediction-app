import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# Load the trained model
model = joblib.load("best_diabetes_model.pkl")

# Define feature names
feature_names = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'Sudden Weight Loss',
                 'Weakness', 'Polyphagia', 'Genital Thrush', 'Visual Blurring',
                 'Itching', 'Irritability', 'Delayed Healing', 'Partial Paresis',
                 'Muscle Stiffness', 'Alopecia', 'Obesity']

def predict_diabetes(input_data, name):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    if prediction == 1:
        message = f"{name} Patient Diagnosed with early-stage diabetes"
    else:
        message = "Individual assessed as low-risk for diabetes"

    return message

def save_user_data(name, contact, address, input_data, prediction_message):
    # Convert 0/1 to Yes/No or Male/Female for CSV
    readable_data = []
    for i, val in enumerate(input_data):
        if feature_names[i] == 'Age':
            readable_data.append(val)
        elif feature_names[i] == 'Gender':
            readable_data.append("Male" if val == 1 else "Female")
        else:
            readable_data.append("Yes" if val == 1 else "No")

    user_data = [name, contact, address] + readable_data + [prediction_message]
    columns = ['Name', 'Contact', 'Address'] + feature_names + ['Prediction']
    df_new = pd.DataFrame([user_data], columns=columns)

    # Save or append to CSV
    if os.path.exists("user_data.csv"):
        df_existing = pd.read_csv("user_data.csv")
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_csv("user_data.csv", index=False)

# Streamlit UI
st.title("Early-Stage Diabetes Prediction")
st.write("Enter the following details to predict the risk of diabetes.")

# User Inputs
name = st.text_input("Enter your name")
contact = st.text_input("Enter your contact")
address = st.text_input("Enter your address")
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

# Encode Inputs for model
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
    prediction_message = predict_diabetes(input_data, name)
    st.subheader(f"Prediction: {prediction_message}")

    # Save user data with readable input and prediction
    save_user_data(name, contact, address, input_data, prediction_message)

    st.success("User data saved successfully!")
