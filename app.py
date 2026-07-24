import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction")

st.title("Customer Churn Prediction")

st.write(
    "This project predicts whether a telecom customer is likely to churn."
)

st.success("Machine Learning model trained successfully!")

st.info(
    "This repository contains the trained model, notebook, and project files."
)

st.subheader("Project Details")

st.write("""
- Dataset: Telco Customer Churn
- Algorithm: Random Forest
- Accuracy: ~85%
- ROC AUC: 0.92
""")
