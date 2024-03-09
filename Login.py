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


st.sidebar.markdown("**Guest Login Credentials**")
st.sidebar.markdown("Username: guest")
st.sidebar.markdown("Password: guest123")

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


if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = False
# Display sidebar and main content only if user is authenticated
if st.session_state["authentication_status"]:
    
    st.write(f'## ♣️Welcome *{st.session_state["name"]}*♣️')
    st.markdown('#### Please proceed to the Home Page🍵')
    if st.button("Home"):
        st.switch_page("Pages/00_🏠_Home.py")
    authenticator.logout()

    
elif st.session_state["authentication_status"] is False:
     st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter username and password provided at sidebar')


# if st.session_state["authentication_status"]:
#     try:
#         if authenticator.reset_password(st.session_state["username"]):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)

# Save updated configuration to YAML file
with open('./config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)






# with open('./config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# authenticator.login()
#
# if st.session_state["authentication_status"]:
#     authenticator.logout()
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     if st.button('Go To Home'):
#           st.switch_page("Pages/00_🏠_Home.py")
#     
#        if menu_selection == "Pages/00_🏠_Home.py":
#             st.switch_page("Pages/00_🏠_Home.py")

#        if menu_selection == "Pages/01_📋_Data.py":
#             st.switch_page("Pages/01_📋_Data.py")
#        if menu_selection == "02_📊_Dashboard.py":
#             st.switch_page("02_📊_Dashboard.py")
#        if menu_selection == "03_📈_Predict.py":
#             st.switch_page("03_📈_Predict.py")
#        if 'user_authenticated' not in st.session_state:
#               st.warning('Please log in to use platform')

#     # if st.button('Go To Home'):
#     #         st.switch_page("Pages/00_🏠_Home.py")

# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')


# with open('./config.yaml', 'w') as file:
#     yaml.dump(config, file, default_flow_style=False)


