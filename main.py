import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px

import pickle

# target = data['Churn']
# features = data[[['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
#        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
#        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
#        'PaperlessBilling', 'PaymentMethod']]

st.set_page_config(
    page_title = 'TELCO CHURN RATE',
    page_icon = "_:home:_",
    layout = "centered",

    )



st.title('Please Register or Login to Access Platform')

import streamlit as st

# Function to register a new user
def register_user(username, email, password):
    # In a real application, you would typically store this information in a database
    registered_users = {"username": username, "email": email, "password": password}
    return registered_users

# Main function
def main():
    st.title("User Registration")

    # Collect user information
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Register button
    if st.button("Register"):
        if username and email and password:
            new_user = register_user(username, email, password)
            st.success("User registered successfully!")
            st.write("Registered User Details:")
            st.write(new_user)
        else:
            st.error("Please fill in all the fields.")

if __name__ == "__main__":





# st.link_button("Go to Home","Pages/00_Home.py") 

 

#st.page_link("Pages/01_Data.py", label="Data")
# st.page_link("Pages/02_Dashboard.py", label="Dashboard")
# st.page_link("Pages/03_Predict.py", label="View Predictions")
# st.page_link("Pages/04_History.py", label="History")
