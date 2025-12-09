import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib

# Load the dataset (for category & language options)
df = pickle.load(open('notebook/MudhithK/df.pkl', 'rb'))

# Load the trained model
pipe = joblib.load('notebook/MudhithK/predict.pkl')

st.title("View Predictor")

# Inputs
category = st.selectbox("Category", df['Category'].unique())
language = st.selectbox("Language", df['Language'].unique())
releaseY = st.number_input("Enter Release Year", min_value=1900, max_value=2030, step=1)
type1 = st.selectbox("Release Month", list(range(1, 13)))
viewY = st.number_input("Enter View Year", min_value=1900, max_value=2030, step=1)
type2 = st.selectbox("Viewing Month", list(range(1, 13)))

if st.button("Predict Views"):

    # Create input DataFrame (this matches model training)
    query = pd.DataFrame({
        "Category": [category],
        "Language": [language],
        "Viewer_Rate": [0], 
        "Release_Year": [releaseY],
        "Release_Month": [type1],
        "Viewing_Year": [viewY],
        "Viewing_Month_Num": [type2]
    })

    # Prediction
    prediction = pipe.predict(query)[0]

    st.subheader("Predicted Number of Views")
    st.title(f"{int(prediction):,}")
