import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px 
import seaborn as sns
from streamlit_date_picker import date_range_picker, PickerType, Unit, date_picker
from streamlit_datetime_range_picker import datetime_range_picker

st.set_page_config(
    page_title = 'Dashboard',
    layout = 'centered'
)

st.selectbox('Select preferred Dashboard',['EDA dashboard','KPI Dashboard'])

datetime_string = datetime_range_picker(unit='minutes', key='range_picker') 
                                        #picker_button={'is_show': True })
if datetime_string is not None:
    start_datetime = datetime_string[0]
    end_datetime = datetime_string[1]

df = pd.read_csv("./Telco_data.csv")

plt.figure(figsize=(12, 4))
data = df.groupby('Churn')['SeniorCitizen'].count()
data.plot(xlabel='SeniorCitizen', ylabel='Churn Count', color ="#86bf91")

# Render the plot using st.pyplot()
st.bar_chart(data)