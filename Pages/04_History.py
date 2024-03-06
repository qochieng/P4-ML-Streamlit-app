import streamlit as st
import pandas as pd 
import numpy as np
from streamlit_date_picker import date_range_picker, PickerType, Unit, date_picker
from streamlit_datetime_range_picker import datetime_range_picker
from PIL import Image
import datetime



st.set_page_config(
    page_title = 'Show History',
    layout = 'wide'
)

st.header("History View")
col1,col2,col3 = st.columns(3)
with col1:
   
    st.subheader('Pick a Date')

with col2:

    date_range_string = date_range_picker(key='range_picker') 
                                        #picker_button={'is_show': True })
if date_range_string  is not None:
    start_date= date_range_string [0]
    end_date = date_range_string [1]
    st.markdown(f'#### Data From {start_date} to {end_date}')

with col3:
    pass

image = Image.open('E:\AZUBI\DATA ANALYTICS\Analytics\PROJECTS\Project 4\P4-ML-Streamlit-app\pics\Ai.jpg')
st.image(image, caption='')

def past_predictions():
   
  path = './data/history.csv'

  df = pd.read_csv(path)

  return df

if __name__ == "__main__":


    df =  past_predictions()

    st.dataframe(df)
