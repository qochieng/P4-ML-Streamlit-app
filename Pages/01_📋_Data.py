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
from st_pages import Page, show_pages, add_page_title
#import toml
# Initialize authentication_status if it's not already initialized
if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = False



 
st.set_page_config(
    page_title= 'View Data',
    page_icon= '📋',
    layout= 'wide'
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
if not st.session_state.authentication_status:
    st.info('Please Login to use Platform.')
    st.stop()


if 'authentication_status' in st.session_state:
    path ="E:\AZUBI\DATA ANALYTICS\Analytics\PROJECTS\Project 4\P4-ML-Streamlit-app\Pages"
    page_selection =st.sidebar.radio ("Go to", ["Login","🏠Home","📋Data" ,"📊Dashboard", "📈Predict", "📚History"])

    if page_selection == "Login.py":
        st.switch_page("Login.py")
    elif page_selection == "🏠Home":
        st.switch_page("pages/00_🏠_Home.py")
    elif page_selection == "📋Data":
        st.switch_page("pages/01_📋_Data.py")
    elif page_selection == "📊Dashboard":
        st.switch_page("pages/02_📊_Dashboard.py")
    elif page_selection == "📈Predict":
        st.switch_page("pages/03_📈_Predict.py")
    elif page_selection == "📚History":
        st.switch_page("pages/04_📚_History.py")
    
    if st.sidebar.button('Logout',key='logout_button'):
        authenticator.logout()
        st.session_state["authentication_status"] = False
        #st.switch_page("Login.py")
# Check authentication status
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


# #Cache connection used to connect database
# @st.cache_resource(show_spinner='Connecting...')
       
#     #Loading environment variables from secret.toml file into a dictionary
# def load_data():
#     environment_variables = st.secrets['Database']


#     #Getting the values for the credentials you set in the '.env' file
#     server = environment_variables['server']
#     database = environment_variables['dbname']
#     username = environment_variables['user']
#     password = environment_variables['password']

#     #Creating a connection string
#     connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;'

#     #establishing a connestion to the database using pyodbc library
#     conn = pyodbc.connect(connection_string)

#     #retrieving data from database
#     query = 'Select * From dbo.LP2_Telco_churn_first_3000'
#     df = pd.read_sql(query,conn)
#     df.to_csv('Telco_churn_3000.csv', index=False)



#     conn.close()
#     return df

# df = load_data()

# Path of the saved data to csv
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

# if st.button("Dashboard"):
#     st.switch_page("Pages/02_📊_Dashboard.py")




