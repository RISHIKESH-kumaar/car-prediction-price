import streamlit as st
import pickle
import pandas as pd

# Load the saved model
with open("linear.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Car Price Prediction App")

# User inputs
year = st.number_input("Enter Car Year", min_value=1990, max_value=2025, step=1)
kms_driven = st.number_input("Enter Kilometers Driven", min_value=0)

company = st.selectbox("Select Company", [
    "BMW", "Chevrolet", "Datsun", "Fiat", "Force", "Ford",
    "Hindustan", "Mahindra", "Maruti", "Mitsubishi", "Nissan",
    "Renault", "Skoda", "Tata", "Toyota", "Volkswagen", "Volvo"
])

fuel = st.selectbox("Select Fuel Type", ["Petrol", "LPG"])

# Predict button
if st.button("Predict Price"):

    # Create input in same format as training data
    input_df = pd.DataFrame(columns=model.feature_names_in_)
    input_df.loc[0] = 0  # set all columns to 0 by default

    input_df["year"] = year
    input_df["kms_driven"] = kms_driven
    input_df[f"company_{company}"] = 1
    input_df[f"fuel_type_{fuel}"] = 1

    prediction = model.predict(input_df)

    st.success(f"Predicted Price: ₹ {int(prediction[0])}")