import streamlit as st
import pandas as pd 
import numpy as np
import joblib
import os
import sklearn
from sqlalchemy import create_engine
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import os
from PIL import Image
from sklearn.preprocessing import OneHotEncoder,LabelEncoder, OrdinalEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from feature_engine.transformation import LogTransformer
import datetime
from Login import login



class LogTransformer():
    def __init__(self, constant=1e-5):
        self.constant = constant
 
    def fit(self, x, y=None):
        return self
    def transform (self,x):
        return np.log1p(x + self.constant)


st.set_page_config(
    page_title = 'Show Predictions',
    layout = 'wide'
)


login()
if st.session_state["authentication_status"] is True:

    st.title = ("Enter Customer Details")

    st.cache_resource(show_spinner='Predicting...')
    def load_Gradient_Model():
        pipeline = joblib.load("./Models/GradientBoosting.pkl")
        return pipeline

    st.cache_resource(show_spinner='Predicting...')
    def load_Random_Model():
        pipeline = joblib.load("./Models/RandomForest.pkl")
        return pipeline

    # Function for Model selection
    def model_selected():
            col1,col2,col3 = st.columns(3)

            with col1:
                
                st.selectbox('Select Model to use:',['Gradient','Random'], key='SelectedModel')

            if st.session_state['SelectedModel']== 'Gradient':      
                pipeline = load_Gradient_Model()

            else:
                pipeline = load_Random_Model()

            encoder = joblib.load('./Models/encoder2.pkl')

            return pipeline,encoder


    if 'prediction' not in st.session_state:
        st.session_state['prediction'] = None

    if 'probability' not in st.session_state:
        st.session_state['probability'] = None

    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None

    # Function for prediction
        
    def make_predict(pipeline,encoder):


        SeniorCitizen = st.session_state['SeniorCitizen']
        gender = st.session_state['gender']
        Partner= st.session_state['Partner']
        Dependents = st.session_state['Dependents']
        PhoneService = st.session_state['phoneService']
        MultipleLines = st.session_state['MultipleLines']
        InternetService = st.session_state['InternetService']
        OnlineSecurity = st.session_state['OnlineSecurity']
        OnlineBackup = st.session_state['Onlinebackup']
        DeviceProtection = st.session_state['DeviceProtection']
        TechSupport = st.session_state['TechSupport']
        StreamingTV = st.session_state['StreamingTV']
        StreamingMovies = st.session_state['StreamingMovies']
        tenure = st.session_state['tenure']
        Contract = st.session_state['contract']
        PaperlessBilling = st.session_state['PaperlessBilling']
        PaymentMethod = st.session_state['PaymentMethod']
        MonthlyCharges = st.session_state['MonthlyCharges']
        TotalCharges = st.session_state['TotalCharges']

        columns = ['SeniorCitizen','gender','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity',
                'OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','tenure','Contract','PaperlessBilling'
                ,'PaymentMethod','MonthlyCharges','TotalCharges']
        
        data = [[SeniorCitizen,gender,Partner,Dependents,PhoneService, MultipleLines,InternetService,OnlineSecurity,
                OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,tenure,Contract,PaperlessBilling
                ,PaymentMethod,MonthlyCharges,TotalCharges]]
        
    # To create a dataframe
        df = pd.DataFrame(data, columns=columns)


        
    
        df['Model'] = st.session_state['SelectedModel']
        prediction = st.session_state['prediction']

        if st.session_state['prediction'] is not None:
           df['Churn'] = ['Yes' if pred == 1 else 'No' for pred in prediction]
        df['Date'] = datetime.date.today()

    

    # Append data to the CSV file, including column names only if writing header
    
        df.to_csv('./data/history.csv', mode='a', header=not os.path.exists('./data/history.csv'), index=False)
        prediction = pipeline.predict(df)
        probability = pipeline.predict_proba(df)

    # To see the state

        st.session_state['prediction'] =prediction
        st.session_state['probability']=probability

        return prediction 

    # Function of form creation

    def display_form():

        pipeline,encoder = model_selected()

        with st.form('Data input', clear_on_submit=True):
            col1, col2, col3 = st.columns(3)

            with col1:
                
                st.write("#### Personal Details")
                SeniorCitizen = st.selectbox('Senior Citizen? No=0, Yes=1',[0,1], key='SeniorCitizen')
                gender = st.selectbox('Select customers gender',['Male','Female'], key='gender')
                Partner = st.selectbox('Has Partner',['True','False'], key='Partner')
                Dependents = st.selectbox('Have Dependents',['True','False'],key='Dependents')
                PhoneService = st.selectbox('Have PhoneService',['True','False'],key='phoneService')
                MultipleLines = st.selectbox('Have MultipleLines',['True','False','None'],key='MultipleLines')
                InternetService = st.selectbox('Which InternetService',['DSL', 'Fiber optic', 'None'],key='InternetService')

            with col2:
                st.write("#### Customer Services")
                OnlineSecurity = st.selectbox('Have OnlineSecurity',['Yes','No'], key='OnlineSecurity')
                OnlineBackup = st.selectbox('Have OnlineBackup',['Yes','No'],key='Onlinebackup')
                DeviceProtection = st.selectbox('Have DeviceProtection',['Yes','No'],key='DeviceProtection')
                TechSupport =  st.selectbox('Have TechSupport',['Yes','No'],key='TechSupport')
                StreamingTV =  st.selectbox('Have StreamingTV',['Yes','No'],key='StreamingTV')
                StreamingMovies = st.selectbox('Have StreamingMovies',['Yes','No'], key='StreamingMovies')         
                
            with col3:
                st.write("#### Payment Details")
                tenure = st.number_input('Customer tenure(months)',0,80, key='tenure')
                Contract =  st.selectbox('Contract Period',['Month-to-month', 'One year', 'Two year'],key='contract')    
                PaperlessBilling = st.selectbox('Use PaperlessBilling',['Yes','No'],key='PaperlessBilling')   
                PaymentMethod = st.selectbox('Payment Method', ["Electronic check","Mailed check", "Bank transfer (automatic)",
                "Credit card (automatic)"],key='PaymentMethod') 
                MonthlyCharges = st.number_input('Average MonthlyCharges',15.0, 120.0,step=1.0,key='MonthlyCharges')  
                TotalCharges = st.number_input('Average TotalCharges',15.0,9000.0,step=10.0,key='TotalCharges')      
                                            

            st.form_submit_button('Predict',on_click=make_predict, kwargs=dict(pipeline=pipeline, encoder=encoder))


    if __name__ == "__main__":
        
        st.markdown("<h1 style='text-align:left;'>Enter Customer Details To Make Prediction</h1>", unsafe_allow_html=True)
        
        
        display_form()


        final_prediction = st.session_state['prediction']
        probability= st.session_state['probability']
        if final_prediction is not None and probability is not None:

            if not os.path.exists('./data/history.csv'):
                os.makedirs('./data', exist_ok=True)
        
            # if not final_prediction:
            #     st.markdown('### Probability will show here')
            if final_prediction == 1:
                probability_of_yes = probability[0][1]*100
                st.markdown(f'#### This Customer will Churn with probability of {round(probability_of_yes,2)}%')
            else:
                probability_of_no = probability[0][0]*100
                st.markdown(f'#### This Customer will not churn with probability of {round(probability_of_no,2)}%')
        else:
            st.markdown('### Probability will show here')

        st.write(st.session_state)





