import streamlit as st
import pandas as pd 
import numpy as np

#from utils import PrepProcesor, columns
#from prediction import predict 
import pickle

#model = pickle.load('Random_Model.pkl')
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

# Gradient = pickle.load("Gradient_model.pkl")
# Random = pickle.load("Random_Model.pkl")


#st.sidebar.title("Pages")
st.title("Welcome To Churn App")
st.subheader("Please Enter Customer Details to Get Churn Prediction")

CustomerId = st.text_input('Input Customers ID:', key='CustomerId')
SeniorCitizen = st.number_input('Is customer a Senior Citizen? No=0, Yes=1',0,1)
gender = st.selectbox('Select customers gender',['Male','Female'])
tenure = st.number_input('What is customer tenure in months',0,80)
Partner = st.selectbox('Does customer have Partner',['True','False'])
Dependants = st.selectbox('Does customer have Dependants',['True','False'])
PhoneService = st.selectbox('Does customer have PhoneService',['True','False'])
MultipleLines = st.selectbox('Does customer have MultipleLines',['True','False','None'])
InternetService = st.selectbox('Which InternetService does customer have',['DSL', 'Fiber optic', 'None'])
OnlineSecurity = st.selectbox('Does customer have OnlineSecurity',['Yes','No'])
OnlineBackup = st.selectbox('Does customer have OnlineBackup',['Yes','No'])
DeviceProtection = st.selectbox('Does customer have DeviceProtection',['Yes','No'])
TechSupport =  st.selectbox('Does customer have TechSupport',['Yes','No'])
StreamingTV =  st.selectbox('Does customer have StreamingTV',['Yes','No'])        
StreamingMovies = st.selectbox('Does customer have StreamingMovies',['Yes','No'])   
Contract =  st.selectbox('What is Customers Contract Period',['Month-to-month', 'One year', 'Two year'])    
PaperlessBilling = st.selectbox('Does customer use PaperlessBilling',['Yes','No'])   
PaymentMethod = st.selectbox('Select Customers payment Method', ["Electronic check","Mailed check", "Bank transfer (automatic)",
"Credit card (automatic)"]) 
MonthlyCharges = st.number_input('What is customer Average MonthlyCharges',key='MonthlyCharges')  
TotalCharges = st.number_input('What is customer Average TotalCharges',key='TotalCharges')      
                            

st.radio("Select the Model Prediction to use",['Gradient','Random'])
if st.button("Predict Customer Churn"):
   st.switch_page("Pages/03_Predict.py") 

# st.page_link("Pages/01_Data.py", label="Data")
# st.page_link("Pages/02_Dashboard.py", label="Dashboard")
# st.page_link("Pages/03_Predict.py", label="View Predictions")
# st.page_link("Pages/04_History.py", label="History")
