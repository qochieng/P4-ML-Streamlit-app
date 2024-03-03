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

data = st.dataframe(df)





# st.title("Data View")

# uploaded_files = st.file_uploader("Choose csv a file")
# if uploaded_files is not None:
#     df = pd.read_csv(uploaded_files)
#     st.write(df)


# df = pd.read_csv("./Telco_data.csv")

# #read csv

# st.title("Telco_Churn Sample Data")  # add a title
# st.write(df) 
