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

# Initialize authentication_status if it's not already initialized


st.set_page_config(
    page_title = 'Home',
    page_icon="🏠",
    layout = 'wide'
)

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
 
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
 
 
name, authentication_status, username = authenticator.login(location='sidebar')

if st.session_state["authentication_status"]:
    authenticator.logout(location='sidebar', key='logout-button')

    st.markdown("<h1 style='text-align:center;'>Welcome to Churn Prediction App</h1>", unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("Churn Prediction")
        st.write('Churn Prediction is a Machine Learning App that helps users to predict the likelihood of a customer leaving or stopping use of the company products')
        st.markdown("##### Key Features")
        st.write('* **Data Page**:Contains sample data used to train the model.')
        st.write('* **Dashboard**:EDA and KPI visualizations for insights.')
        st.write('* **Predict Page**:Shows prediction for Customer Churn.')
        st.write('* **History Page**:Shows past predictions made.')
        st.write('* **Feedback Page**:Leave a comment or feedback about the app.')

        st.markdown("##### User Benefits")
        st.write('* **Real time Prediction**: User is able to make predictions.')
        st.write('* **Easy Machine Learning**: Utilize powerful machine learning effortlessly.')

    with col2:

        st.text_area("#### How to run the App","Activate virtual environment\nvenv/Scripts/activate\n Streamlit run Login.py",disabled=True)
        st.markdown('### Machine Learning Intergration')
        st.write('* **Model Selection**: Choose between two powerful models')
        st.write('* **Seamless Intergration**: Intergrate predictions into your workflow with a user-friendly interface')
        st.write('* **Probability Estimates**: gain Insights into the likelihood of an outcome')

        st.markdown('### Need Help?')
        st.write('**Contact me at**: qochieng88@outlook.com')
        st.link_button("App Github Repository","https://github.com/qochieng/P4-ML-Streamlit-app")

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.info('Enter username and password to use the app.')

# if st.button("Next"):
#     st.switch_page("Pages/01_📋_Data.py")



