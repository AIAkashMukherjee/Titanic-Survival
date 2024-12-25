# app.py
import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.prediction_pipeline import PredicitonPipe  # Assuming prediction_pipe.py is in the same directory

# Initialize the Prediction Pipeline
prediction_pipe = PredicitonPipe()

# Title and description for the app
st.title("Titanic Survival Prediction")
st.write("This app predicts if a passenger survived or not based on their information.")

# User input form to get passenger details
with st.form(key='prediction_form'):
    # Numeric inputs (e.g., Age, Fare)
    age = st.number_input('Age', min_value=0, max_value=76, value=30)
    fare = st.number_input('Fare', min_value=0.0, value=7.25,max_value=512.33)
    sibsp = st.number_input('SibSp (Siblings/Spouses aboard)', min_value=0, value=0,max_value=8)
    parch = st.number_input('Parch (Parents/Children aboard)', min_value=0, value=0,max_value=9)
    
    # Categorical inputs (e.g., Sex, Embarked)
    sex = st.selectbox('Sex', ['male', 'female'])
    embarked = st.selectbox('Embarked', ['C', 'Q', 'S'])
    
    # Other features if necessary
    pclass = st.selectbox('Pclass (Ticket Class)', [1, 2, 3])
    
    # Submit button
    submit_button = st.form_submit_button(label='Predict')

# Prepare input data for prediction
if submit_button:
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'Age': [age],
        'Fare': [fare],
        'Sex': [sex],
        'Embarked': [embarked],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Pclass': [pclass]
    })

    # Get prediction using the PredictionPipe
    prediction = prediction_pipe.predict(input_data)
    
    # Display the prediction result
    if prediction == 1:
        st.markdown('<div style="background-color: green; color: white; padding: 10px; border-radius: 5px;">The passenger <strong>survived</strong>.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: red; color: white; padding: 10px; border-radius: 5px;">The passenger <strong>did not survive</strong>.</div>', unsafe_allow_html=True)
