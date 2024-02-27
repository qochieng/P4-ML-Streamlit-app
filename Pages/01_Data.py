import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title = 'View Data',
    layout = 'centered'
)

st.title("Data View")

uploaded_files = st.file_uploader("Choose csv a file")
if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    st.write(df)


df = pd.read_csv("./Telco_data.csv")

#read csv

st.title("Telco_Churn Sample Data")  # add a title
st.write(df) 
