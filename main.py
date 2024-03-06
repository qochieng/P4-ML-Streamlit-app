import streamlit as st
import pandas as pd 
import numpy as np
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
#from pathlib import path 
import os
from PIL import Image

import pickle



#st.markdown("",unsafe_allow_html=True)
#st.image('sunrise.jpg')

st.set_page_config(
    page_title = 'TELCO CHURN RATE',
    page_icon = "🏠",
    layout = "centered",

    )

bg_image_path = "https://images.app.goo.gl/47yNcjPmLJATeDKS7"

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("{bg_image_path}");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack_url()


with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    if st.button('Go To Home'):
            st.switch_page("Pages/00_Home.py")
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

# Password Reset
if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

# Updating Details
if st.session_state["authentication_status"]:
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)

# New User Registration

try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(preauthorization=False)
    if email_of_registered_user:
        st.success('User registered successfully')
except Exception as e:
    st.error(e)

# # Forgot Password Reset
# try:
#     username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
#     if username_of_forgotten_password:
#         st.success('New password to be sent securely')
#         # The developer should securely transfer the new password to the user.
#     elif username_of_forgotten_password == False:
#         st.error('Username not found')
# except Exception as e:
#     st.error(e)  
# # Forgot User Reset
# try:
#     username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
#     if username_of_forgotten_username:
#         st.success('Username to be sent securely')
#         # The developer should securely transfer the username to the user.
#     elif username_of_forgotten_username == False:
#         st.error('Email not found')
# except Exception as e:
#     st.error(e)  



with open('./config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)








# st.title("User Login")

# username = st.text_input("Username",key="username")
# password = st.text_input("Password", key="password")

# # Button to submit the login form
# if st.button("Login"):
#     # Dummy authentication (replace with actual authentication logic)
#    if username == "admin" and password == "password":
#       st.page_link("Pages/00_Home.py")
#    else:
#       st.error("Invalid username or password")

# #st.link_button("Login","Pages/00_Home.py") 



# st.title("User Registration Form")

# # Input fields for username, email, password, and bio
# username = st.text_input("Username")
# email = st.text_input("Email")
# password = st.text_input("Password", type="password")


# # Checkbox for agreeing to terms and conditions
# agree_terms = st.checkbox("I agree to the terms and conditions")

# # Button to submit the registration form
# if st.button("Register"):
#     # Validation checks
#     if not username:
#         st.error("Please enter a username")
#     elif not email:
#         st.error("Please enter an email")
#     elif not password:
#         st.error("Please enter a password")
#     elif not agree_terms:
#         st.error("Please agree to the terms and conditions")
#     else:
#         # Registration logic (e.g., save to database)
#         st.form_submit_button("Register")




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
    