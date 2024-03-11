import streamlit as st
import pandas as pd
import numpy as np

#Import modules and packages to be used
import streamlit as st
import pandas as pd
import pyodbc
import toml
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
#from pathlib import path 
import os
from PIL import Image

#import toml
# Initialize authentication_status if it's not already initialized


st.set_page_config(
    page_title= 'View Data',
    page_icon= '📋',
    layout= 'wide'
)


if not st.session_state.get("authentication_status"):
    st.info('Please Login to use Platform.')
else:
     
    st.markdown("<h1 style='text-align:left;'>Proprietory Data from Vodafone</h1>", unsafe_allow_html=True)
    st.title = ('Data from Vodafone')

    expand = st.expander(f"### Column Description:")

    expand.write(f" Gender-- Whether the customer is a male or a female")
    expand.write(f" SeniorCitizen -- Whether a customer is a senior citizen or not")
    expand.write(f" Partner -- Whether the customer has a partner or not")
    expand.write(f" Dependents -- Whether the customer has dependents or not")
    expand.write(f" Tenure -- Number of months the customer has stayed with the company")
    expand.write(f" Phone Service -- Whether the customer has a phone service or not")
    expand.write(f" MultipleLines -- Whether the customer has multiple lines or not")
    expand.write(f" InternetService -- Customer's internet service provider (DSL, Fiber Optic, No)")
    expand.write(f" OnlineSecurity -- Whether the customer has online security or not (Yes, No, No Internet)")
    expand.write(f" OnlineBackup -- Whether the customer has online backup or not (Yes, No, No Internet)")
    expand.write(f" DeviceProtection -- Whether the customer has device protection or not (Yes, No, No internet service)")
    expand.write(f" TechSupport -- Whether the customer has tech support or not (Yes, No, No internet)")
    expand.write(f" StreamingTV -- Whether the customer has streaming TV or not (Yes, No, No internet service)")
    expand.write(f" StreamingMovies -- Whether the customer has streaming movies or not (Yes, No, No Internet service)")
    expand.write(f" Contract -- The contract term of the customer (Month-to-Month, One year, Two year)")
    expand.write(f" PaperlessBilling -- Whether the customer has paperless billing or not (Yes, No)")
    expand.write(f" Payment Method -- The customer's payment method ")
    expand.write(f" MonthlyCharges -- The amount charged to the customer monthly")



    path = './data/Telco_churn_3000.csv'
    # To read the file as CSV
    df = pd.read_csv(path)

    column_selected = st.selectbox('Column Type:', ['Numeric', 'Categorical', 'All columns'], key='columnselected')

    # Display DataFrame based on selected data type
    if column_selected == 'Numeric':
        st.dataframe(df.select_dtypes(include=['number']))
    elif column_selected == 'Categorical':
        st.dataframe(df.select_dtypes(include=['object','bool']))
    else:
        st.dataframe(df)






