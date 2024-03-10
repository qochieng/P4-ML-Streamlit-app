import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px 
import seaborn as sns
from streamlit_date_picker import date_range_picker, PickerType, Unit, date_picker
from streamlit_datetime_range_picker import datetime_range_picker
st.set_option('deprecation.showPyplotGlobalUse', False)
if not st.session_state.authentication_status:
    st.info('Please Login to use Platform.')
    st.stop()

st.set_page_config(
    page_title = 'Dashboard',
    layout = 'wide'
)


path = "./data/Telco_data.csv"
df =pd.read_csv(path)

# Function for EDA dashboard

def EDA():

      col1, col2, col3,col4 = st.columns(4)

        
      with col1:
            

            Contract_type = df['Contract'].value_counts().reset_index()
            Contract_type.columns = ['Contract', 'count']
            fig = px.bar(Contract_type, x='Contract', y='count', color='Contract', color_discrete_map={'Month-to-month': 'pink', 'One year': 'skyblue', 'Two year': 'grey'})
            fig.update_layout(title='Churn based on Contract',width=500, height=500)

            st.plotly_chart(fig)


            data= df['tenure']
            fig = px.histogram(df, x='tenure', color='tenure', color_discrete_sequence=['pink'])
            fig.update_layout(title='Tenure Distribution',width=500, height=500)
            st.plotly_chart(fig)

    

      with col4:


            data = df[['tenure', 'TotalCharges', 'MonthlyCharges','Churn']]
            fig = px.box(data, color='Churn', notched=True,)
            fig.update_layout(title='Box Plots for Numerical Data')
            fig.update_layout(height=500, width=500)
            st.plotly_chart(fig)


              #  Empirical Cumulative Distribution Function (ECDF) charts.

            df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

            churn_rate_by_tenure = df.groupby(['gender', 'tenure'])['Churn'].mean().reset_index(name='count')
            # Sorting the values by 'tenure' within each gender group
            churn_rate_by_tenure.sort_values(by=['gender', 'tenure'], inplace=True)
            # Calculating the cumulative sum of the churn rate within each gender group
            churn_rate_by_tenure['cum_count'] = churn_rate_by_tenure.groupby('gender')['count'].cumsum()
            # Creating the ECDF plot using Plotly Express
            fig = px.line(churn_rate_by_tenure, x='tenure', y='cum_count', color='gender', color_discrete_map={'Female': 'blue', 'Male': 'pink'},
                        title='Churn Rate vs Tenure by Gender', 
                        labels={'cum_count': 'Churn Rate'})
            # Update layout
            fig.update_layout( xaxis_title='Tenure', yaxis_title='Churn Rate',width=500, height=500)
            # Display the chart using Streamlit
            st.plotly_chart(fig)


# Violin plots is a statistical representation of numerical data. It is similar to a box plot,
      with col2:
           pass            
# Function for KPI dashboard
      
 

def KPI():

    col1,col2,col3,col4,col5,col6,col7 = st.columns(7)

    with col1:

     
        data = df[['gender', 'Churn']]
        churn_counts = data.groupby('gender')['Churn'].value_counts().unstack(fill_value=0)
        fig = px.pie(names=churn_counts.index, values=churn_counts['Yes'], color=churn_counts.index,color_discrete_map={'Female': 'pink', 'Male': 'skyblue'},
                    title='Churn Rate by Gender', labels={'Churn': 'Churned', 'gender': 'Gender'},hole=0.3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)

        # Violin plots is a statistical representation of numerical data. It is similar to a box plot,

        data = df['TotalCharges']
        fig = px.violin(data, title='Total Charges Distribution',y="TotalCharges",width=500, height=500)
        st.plotly_chart(fig)


    with col7:
         
         data = df[['Churn']]
         churn_counts = data['Churn'].value_counts()
         fig = px.pie(names=churn_counts.index, values=churn_counts.values,
                    title='Number of Customers Churned')
         fig.update_traces(pull=[0, 0.1])  #desired explosion effect
         fig.update_traces(textposition='inside', textinfo='percent+label') 
         st.plotly_chart(fig)


         data = df[['gender', 'TotalCharges']]
         churn_counts = data.groupby('gender')['TotalCharges'].sum().reset_index()
         fig.update_layout(title='Tenure Distribution',width=400, height=500)
         fig = px.bar(churn_counts, x='gender', y='TotalCharges',title="Average Sum Charges per gender" ,color='gender',labels={'TotalCharges': 'TotalCharges', 'gender': 'Gender'},color_discrete_map={'Female': 'pink', 'Male': 'grey'},)
        
         st.plotly_chart(fig)


    with col2:
         
         def plot_payment_methods(df):
                payment_counts = df['PaymentMethod'].value_counts().reset_index()
                payment_counts.columns = ['PaymentMethod', 'count']
                fig = px.bar(payment_counts, x='PaymentMethod', y='count', color='PaymentMethod', color_discrete_map={'Bank transfer (automatic)': 'pink', 'Credit card (automatic)': 'skyblue', 'Electronic check': 'violet', 'Mailed check': 'grey'})
                fig.update_layout(title='Payment Methods')
                st.plotly_chart(fig)

    plot_payment_methods(df)
    

# Function to instantiate the selected dashboard

def dashboard():

    st.markdown("<h1 style='text-align:left;'>Welcome to our Dashboard</h1>", unsafe_allow_html=True)

    st.selectbox('Select dashboard type',['EDA dashboard','KPI dashboard'],key='dashSelected')

    col1, col2 = st.columns(2)

    with col1:
         
        if st.session_state['dashSelected']=='EDA dashboard':
            EDA()

        if st.session_state['dashSelected']=='KPI dashboard':
            KPI()

    with col2:
         pass



if __name__ == "__main__":

    dashboard()