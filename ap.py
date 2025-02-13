import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("svm.pkl")

# Streamlit UI
st.title("💧 Water Quality Prediction App")

st.write("Enter the water quality parameters below to predict whether the water is **Safe** or **Unsafe**.")

# User input fields
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=100.0)
solids = st.number_input("Solids", min_value=0.0, value=10000.0)
chloramines = st.number_input("Chloramines", min_value=0.0, value=5.0)
sulfate = st.number_input("Sulfate", min_value=0.0, value=300.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)
organicCarbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=50.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=3.0)

# Prediction button
if st.button("🔍 Predict Water Quality"):
    # Prepare input data
    input_values = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organicCarbon, trihalomethanes, turbidity]])
    
    # Make prediction
    prediction = model.predict(input_values)[0]

    # Convert prediction to readable format
    prediction_label = "✅ Safe" if prediction == 1 else "❌ Unsafe"

    # Display result
    st.subheader(f"Prediction: {prediction_label}")
