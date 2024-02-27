import streamlit as st
import pandas as pd 
import numpy as np
import joblib
import sklearn
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, RobustScaler,FunctionTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder, OrdinalEncoder
from sklearn.base import BaseEstimator, TransformerMixin
#from sktime.transformations.series.boxcox import LogTransformer
from feature_engine.transformation import LogTransformer

class LogTransformer():
    def __init__(self, constant=1e-5):
        self.constant = constant
 
    def fit(self, x, y=None):
        return self
    def transform (self,x):
        return np.log1p(x + self.constant)


st.set_page_config(
    page_title = 'Show Predictions',
    layout = 'centered'
)

st.title = ("Enter Customer Details")

st.cache_resource(show_spinner='Predicting...')
def load_Gradient_Model():
    pipeline = joblib.load("./Models/Gradient_boosting_model.joblib")
    return pipeline

st.cache_resource(show_spinner='Predicting...')
def load_Linear_Model():
    pipeline = joblib.load("./Models/Linear_model.joblib")
    return pipeline

# # Function for Model selection
def model_selected():
    
    
    Selected_model = st.selectbox('Select Model to use:',['Gradient','Linear'], key='SelectedModel')

    # if Selected_model== 'Gradient':      
    #   pipeline = load_Gradient_Model()

    # else:
    #   pipeline = load_Linear_Model()

    # encoder = joblib.load('./Models/encoder..joblib')

    #return pipeline,encoder

# # # Function for prediction
    
def make_predict(pipeline, encoder):

    SeniorCitizen = st.session_state['SeniorCitizen']
    gender = st.session_state['gender']
    Partner= st.session_state['Partner']
    Dependants = st.session_state['Dependants']
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

    columns = ['SeniorCitizen','gender','Partner','Dependants','PhoneService','MultipleLines','InternetService','OnlineSecurity',
            'OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','tenure','Contract','PaperlessBilling'
            ,'PaymentMethod','MonthlyCharges','TotalCharges']
    
    data = [[SeniorCitizen,gender,Partner,Dependants,PhoneService, MultipleLines,InternetService,OnlineSecurity,
            OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,tenure,Contract,PaperlessBilling
            ,PaymentMethod,MonthlyCharges,TotalCharges]]
    
    df = pd.DataFrame(data, columns=columns)

    prediction = pipeline.predict(df)
    st.session_state['prediction'] = prediction

    return prediction



def display_form():

    with st.form('Data input'):

        #pipeline,encoder = model_selected()
    

        col1, col2, col3 = st.columns(3)

        with col1:
            
            #CustomerId = st.text_input('Input Customers ID:', key='CustomerId')
            st.write("#### Personal Details")
            SeniorCitizen = st.selectbox('Senior Citizen? No=0, Yes=1',[0,1], key='SeniorCitizen')
            gender = st.selectbox('Select customers gender',['Male','Female'], key='gender')
            Partner = st.selectbox('have Partner',['True','False'], key='Partner')
            Dependants = st.selectbox('have Dependants',['True','False'],key='Dependants')
            PhoneService = st.selectbox('have PhoneService',['True','False'],key='phoneService')
            MultipleLines = st.selectbox('have MultipleLines',['True','False','None'],key='MultipleLines')
            InternetService = st.selectbox('Which InternetService',['DSL', 'Fiber optic', 'None'],key='InternetService')

        with col2:
            st.write("#### Customer Services")
            OnlineSecurity = st.selectbox('have OnlineSecurity',['Yes','No'], key='OnlineSecurity')
            OnlineBackup = st.selectbox('have OnlineBackup',['Yes','No'],key='Onlinebackup')
            DeviceProtection = st.selectbox('have DeviceProtection',['Yes','No'],key='DeviceProtection')
            TechSupport =  st.selectbox('have TechSupport',['Yes','No'],key='TechSupport')
            StreamingTV =  st.selectbox('have StreamingTV',['Yes','No'],key='StreamingTV')
            StreamingMovies = st.selectbox('have StreamingMovies',['Yes','No'], key='StreamingMovies')         
            
        with col3:
            st.write("#### Payment Details")
            tenure = st.number_input('customer tenure(months)',0,80, key='tenure')
            Contract =  st.selectbox('Contract Period',['Month-to-month', 'One year', 'Two year'],key='contract')    
            PaperlessBilling = st.selectbox('use PaperlessBilling',['Yes','No'],key='PaperlessBilling')   
            PaymentMethod = st.selectbox('payment Method', ["Electronic check","Mailed check", "Bank transfer (automatic)",
            "Credit card (automatic)"],key='PaymentMethod') 
            MonthlyCharges = st.number_input('Average MonthlyCharges',15.0, 120.0,step=1.0,key='MonthlyCharges')  
            TotalCharges = st.number_input('Average TotalCharges',15.0,9000.0,step=10.0,key='TotalCharges')      
                                        

        submit_button = st.form_submit_button('Predict')

        if submit_button:
            pipeline, encoder= model_selected()
            make_predict(pipeline, encoder)




        #st.form_submit_button('Predict',on_click=make_predict, kwargs=dict(pipeline=model, encoder=encoder))

if __name__ == "__main__":
     #model_selected()
     #st.selectbox('Select Model to use:'['Gradient','Linear'])
     st.header("Enter Customer Details")
     model_selected()
   
     display_form()

     final_prediction = st.session_state['prediction']
     st.markdown('##{final_prediction}')
  


     st.session_state(key='prediction')



#[gender ,SeniorCitizen,Partner ,Dependents,tenure,PhoneService ,MultipleLines ,
#InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,
#Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]

