import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title = 'View Data',
    layout = 'centered'
)

st.title("Data View")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)