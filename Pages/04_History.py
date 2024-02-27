import streamlit as st
import pandas as pd 
import numpy as np
from streamlit_date_picker import date_range_picker, PickerType, Unit, date_picker
from streamlit_datetime_range_picker import datetime_range_picker
from PIL import Image



st.set_page_config(
    page_title = 'Show History',
    layout = 'centered'
)

st.header("History View")

st.markdown(f'### Pick a Date')
datetime_string = datetime_range_picker(unit='minutes', key='range_picker') 
                                        #picker_button={'is_show': True })
if datetime_string is not None:
    start_datetime = datetime_string[0]
    end_datetime = datetime_string[1]

image = Image.open('E:\AZUBI\DATA ANALYTICS\Analytics\PROJECTS\Project 4\P4-ML-Streamlit-app\pics\Ai.jpg')
st.image(image, caption='')