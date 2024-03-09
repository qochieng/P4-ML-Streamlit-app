import streamlit as st
import pandas as pd
import numpy as np

# Initialize authentication_status if it's not already initialized
if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = False

# Check authentication status
if not st.session_state.authentication_status:
    st.info('Please Login to use Platform.')
    st.stop()

st.set_page_config(
    page_title = 'Home',
    page_icon="🏠",
    layout = 'wide'
)
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


# if st.button("Next"):
#     st.switch_page("Pages/01_📋_Data.py")



