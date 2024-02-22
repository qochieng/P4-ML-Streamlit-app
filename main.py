import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
#from pathlib import path 
import os

import pickle

# target = data['Churn']
# features = data[[['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
#        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
#        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
#        'PaperlessBilling', 'PaymentMethod']]

st.set_page_config(
    page_title = 'TELCO CHURN RATE',
    page_icon = ":home:",
    layout = "centered",

    )

st.title('Please Login to Access Platform')

# file_path = path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)

# authenticator =stauth.Authenticate(names, usernames, hashed_passwords,"00_Home.py", "cdefg", cookie_expiry_days=30)

# name, authentication_status, username = authenticator.login("Login", "00_Home.py")

# if authentication_status == False:
#     st.error("Username/Password is Incorrect")
# if authentication_status == None:
#     st.warning("Enter Username and Password")
# if authentication_status== True:
#     st.page_link("Pages/00_Home.py", label="Login")




st.title("User Login")

username = st.text_input("Username",key="username")
password = st.text_input("Password", key="password")

# Button to submit the login form
if st.button("Login"):
    # Dummy authentication (replace with actual authentication logic)
   if username == "admin" and password == "password":
      st.page_link("Pages/00_Home.py")
   else:
      st.error("Invalid username or password")

#st.link_button("Login","Pages/00_Home.py") 



st.title("User Registration Form")

# Input fields for username, email, password, and bio
username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")


# Checkbox for agreeing to terms and conditions
agree_terms = st.checkbox("I agree to the terms and conditions")

# Button to submit the registration form
if st.button("Register"):
    # Validation checks
    if not username:
        st.error("Please enter a username")
    elif not email:
        st.error("Please enter an email")
    elif not password:
        st.error("Please enter a password")
    elif not agree_terms:
        st.error("Please agree to the terms and conditions")
    else:
        # Registration logic (e.g., save to database)
        st.form_submit_button("Register")




# # Function to display registration form
# def registration_form():
#     st.title("User Registration Form")
#     # Your registration form code here...

# # Function to display login form
# def login_form():
#     st.title("User Login")
#     # Your login form code here...

# # Main application
# def main():
#     st.sidebar.title("Navigation")
#     option = st.sidebar.radio("Go to", ["Home", "Registration", "Login"])

#     if option == "Home":
#         st.title("Welcome to Streamlit App")
#         st.write("This is the home page.")

#     elif option == "Registration":
#         registration_form()

#     elif option == "Login":
#         login_form()

# # Run the main application
# if __name__ == "__main__":
#     main()

 

#st.page_link("Pages/01_Data.py", label="Data")
# st.page_link("Pages/02_Dashboard.py", label="Dashboard")
# st.page_link("Pages/03_Predict.py", label="View Predictions")
# st.page_link("Pages/04_History.py", label="History")
    