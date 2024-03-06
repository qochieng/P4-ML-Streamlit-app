import streamlit as st
import pandas as pd
import numpy as np

#Import modules and packages to be used
import streamlit as st
import pandas as pd
import pyodbc
import toml
#import toml

 
st.set_page_config(
    page_title= 'View Data',
    page_icon= '',
    layout= 'wide'
)
st.header('Sample Data from Vodafone')

st.title = ('Data from Vodafone')



#Cache connection used to connect database
@st.cache_resource(show_spinner='Connecting...')
       
    #Loading environment variables from secret.toml file into a dictionary
def load_data():
    environment_variables = st.secrets['Database']


    #Getting the values for the credentials you set in the '.env' file
    server = environment_variables['server']
    database = environment_variables['dbname']
    username = environment_variables['user']
    password = environment_variables['password']

    #Creating a connection string
    connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;'

    #establishing a connestion to the database using pyodbc library
    conn = pyodbc.connect(connection_string)

    #retrieving data from database
    query = 'Select * From dbo.LP2_Telco_churn_first_3000'
    df = pd.read_sql(query,conn)


    conn.close()
    return df


df = load_data()

column_selected = st.selectbox('Column Type:', ['Numeric', 'Categorical', 'All columns'], key='columnselected')

# Display DataFrame based on selected data type
if column_selected == 'Numeric':
    st.dataframe(df.select_dtypes(include=['number']))
elif column_selected == 'Categorical':
    st.dataframe(df.select_dtypes(include=['object','bool']))
else:
    st.dataframe(df)

if st.button("Dashboard"):
    st.switch_page("Pages/02_Dashboard.py")

st.markdown('##### Column Description:')

st.markdown(f" Gender: Whether the customer is a male or a female")
st.markdown(f" SeniorCitizen -- Whether a customer is a senior citizen or not")
st.markdown(f" Partner -- Whether the customer has a partner or not")
st.markdown(f" Dependents -- Whether the customer has dependents or not")
st.markdown(f" Tenure -- Number of months the customer has stayed with the company")
st.markdown(f" Phone Service -- Whether the customer has a phone service or not")
st.markdown(f" MultipleLines -- Whether the customer has multiple lines or not")
st.markdown(f" InternetService -- Customer's internet service provider (DSL, Fiber Optic, No)")
st.markdown(f" OnlineSecurity -- Whether the customer has online security or not (Yes, No, No Internet)")
st.markdown(f" OnlineBackup -- Whether the customer has online backup or not (Yes, No, No Internet)")
st.markdown(f" DeviceProtection -- Whether the customer has device protection or not (Yes, No, No internet service)")
st.markdown(f" TechSupport -- Whether the customer has tech support or not (Yes, No, No internet)")
st.markdown(f" StreamingTV -- Whether the customer has streaming TV or not (Yes, No, No internet service)")
st.markdown(f" StreamingMovies -- Whether the customer has streaming movies or not (Yes, No, No Internet service)")
st.markdown(f" Contract -- The contract term of the customer (Month-to-Month, One year, Two year)")
st.markdown(f" PaperlessBilling -- Whether the customer has paperless billing or not (Yes, No)")
st.markdown(f" Payment Method -- The customer's payment method ")
st.markdown(f" MonthlyCharges -- The amount charged to the customer monthly")



# st.title("Data View")

# uploaded_files = st.file_uploader("Choose csv a file")
# if uploaded_files is not None:
#     df = pd.read_csv(uploaded_files)
#     st.write(df)


# df = pd.read_csv("./Telco_data.csv")

# #read csv

# st.title("Telco_Churn Sample Data")  # add a title
# st.write(df) 
