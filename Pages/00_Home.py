import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title = 'Home',
    page_icon="🏠",
    layout = 'centered'
)

st.header("Welcome to Churn Prediction App")

st.subheader("Below are the steps to be followed:")

st.markdown("STEP 1: \n##### Fill in the form")


st.markdown(f"STEP 2: \n##### Select the type of Model")

st.markdown(f"STEP 3: \n##### Get Prediction")

st.markdown("STEP 4: \n##### Generate Report")



if st.button("Next"):
    st.switch_page("Pages/01_Data.py")



