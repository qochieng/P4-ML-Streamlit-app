import streamlit as st
import pandas as pd 
import numpy as np
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
#from pathlib import path 
import os
from PIL import Image
from st_pages import Page, show_pages, add_page_title
from streamlit_option_menu import option_menu


import pickle



st.set_page_config(
    page_title='TELCO CHURN RATE',
    page_icon="🏠",
    layout="wide"
)

# Load configuration from YAML file
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Authenticate user
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()


# Display login information
st.markdown("**Guest Login Credentials**")
st.markdown("Username: guest")
st.markdown("Password: guest123")

# Display sidebar and main content only if user is authenticated
if st.session_state.get("authentication_status"):
    st.write(f'## ♣️Welcome *{st.session_state["name"]}*♣️')
    
#if 'authentication_status' in st.session_state:
    page_selection = st.sidebar.radio("Go to", ["Login","🏠Home","📋Data" ,"📊Dashboard", "📈Predict", "📚History"])
    if page_selection == "Login.py":
        st.switch_page("Login.py")
    elif page_selection == "🏠Home":
        st.switch_page("Pages/00_🏠_Home.py")
    elif page_selection == "📋Data":
        st.switch_page("Pages/01_📋_Data.py")
    elif page_selection == "📊Dashboard":
        st.switch_page("Pages/02_📊_Dashboard.py")
    elif page_selection == "📈Predict":
        st.switch_page("Pages/03_📈_Predict.py")
    elif page_selection == "📚History":
        st.switch_page("Pages/04_📚_History.py")
    
    #if st.sidebar.button('Logout',key='logout_button'):
    authenticator.logout()
        #st.session_state["authentication_status"] = False
else:
    if st.session_state.get("authentication_status") is False:
        st.error('Please enter the username and password provided above')
    else:
        st.warning('Username/password is incorrect')


with open('./config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
# if st.session_state["authentication_status"]:
    # try:
    #     if authenticator.reset_password(st.session_state["username"]):
    #         st.success('Password modified successfully')
    # except Exception as e:
    #     st.error(e)

#Save updated configuration to YAML file








# with open('./config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# # Authenticate user
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# authenticator.login()

# # Check authentication status and manage session states
# if st.session_state.get("authentication_status"):
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     if st.button('Go To Home'):
#         st.switch_page("Pages/00_🏠_Home.py")
#     authenticator.logout()
#     menu_selection = st.selectbox("Select page", ["Login","Home", "Data", "Dashboard", "Predict"])
#     if menu_selection == "Login":
#         st.switch_page("Login.py")
#     if menu_selection == "Home":
#         st.switch_page("Pages/00_🏠_Home.py")
#     elif menu_selection == "Data":
#         st.switch_page("Pages/01_📋_Data.py")
#     elif menu_selection == "Dashboard":
#         st.switch_page("02_📊_Dashboard.py")
#     elif menu_selection == "Predict":
#         st.switch_page("03_📈_Predict.py")
#     st.write('---')
# if st.button('Logout'):
#         authenticator.logout()
#         st.session_state["authentication_status"] = False
#         st.write('You have been logged out. Please log in again.')
# else:
#     st.error('Username/password is incorrect' if st.session_state.get("authentication_status") is False else 'Please enter your username and password')
# # Save the updated configuration back to the YAML file
# with open('./config.yaml', 'w') as file:
#     yaml.dump(config, file, default_flow_style=False)


