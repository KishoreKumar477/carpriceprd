import streamlit as st
import pandas as pd
import joblib

st.title("🚗 Car Price Prediction")

# Load trained model
model = joblib.load("model.pkl")

# Inputs
year = st.number_input("Year", 1990, 2025, 2018)
present_price = st.number_input("Present Price")
kms_driven = st.number_input("Kms Driven")
owner = st.selectbox("Owner", [0, 1, 2, 3])

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Manual Encoding (must match training encoding)
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
transmission_map = {"Manual": 0, "Automatic": 1}

fuel_encoded = fuel_map[fuel_type]
seller_encoded = seller_map[seller_type]
transmission_encoded = transmission_map[transmission]

if st.button("Predict"):
    input_df = pd.DataFrame({
        "Year": [year],
        "Present_Price": [present_price],
        "Kms_Driven": [kms_driven],
        "Fuel_Type": [fuel_encoded],
        "Seller_Type": [seller_encoded],
        "Transmission": [transmission_encoded],
        "Owner": [owner]
    })

# Ensure exact column order used during training
    input_df = input_df[
        ["Year", "Present_Price", "Kms_Driven",
        "Fuel_Type", "Seller_Type", "Transmission", "Owner"]]
    if present_price <= 0:
        st.error("Present Price must be greater than 0")
    else:
        prediction = model.predict(input_df)
        st.success(f"Predicted Price: ₹ {prediction[0]:.2f} Lakhs")

    