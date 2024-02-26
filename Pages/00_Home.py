import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title = 'Home',
    page_icon="🏠",
    layout = 'centered'
)

st.title("Welcome to Churn Prediction App")

st.header("Below are the steps to be followed:")

st.subheader("STEP 1: \n##### Upload data/Fill in the form")


st.subheader(f"STEP 2: \n##### Select the type of Model")

st.subheader(f"STEP 3: \n##### Get Prediction")

st.subheader("STEP 4: \n##### Generate Report")



st.link_button("Next", "Pages/01_Data.py")

