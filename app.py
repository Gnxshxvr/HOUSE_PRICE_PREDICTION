import streamlit as st
import numpy as np
import joblib

# Load the pre-trained house price prediction model from pickle file
model = joblib.load('HousePriceModel.pkl')

st.divider()

st.title("🏠 House Price Prediction - Ganeshvar")

st.divider()

st.write("Enter the details of the house to predict its price:")

st.divider()

# Create input fields for the model features (assumes order: bedrooms, bathrooms, livingarea, condition, numberofschools)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=8, value=2)                     
livingarea = st.number_input("Living Area (sqft)", min_value=500, max_value=10000, value=2000)
condition = st.number_input("Condition (1-5)", min_value=1, max_value=5, value=3)
numberofschools = st.number_input("Number of Schools Nearby", min_value=0, max_value=10, value=2)

st.divider()

# Prepare feature vector for prediction (must match model training features exactly)
x = [[bedrooms, bathrooms, livingarea, condition, numberofschools]]
X_array = np.array(x)

# Create prediction button
predict_button = st.button("🔮 Predict Price")

if predict_button:
    # Make prediction using the loaded model
    predicted_price = model.predict(X_array)[0]  # Extract scalar from array
    
    st.balloons()
    
    # Display formatted prediction
    st.success(f"**Predicted House Price: ₹{predicted_price:,.2f}**")
    
else:
    st.info("👆 Enter details above and click 'Predict Price' to get the estimated value.")

st.divider()
