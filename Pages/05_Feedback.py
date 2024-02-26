import streamlit as st
import pandas as pd 
import numpy as np


st.set_page_config(
    page_title = 'Feedback Page',
    layout = 'centered'
)


def Feedback_form():

   with st.form('Feedback Form'):
   


    st.title("Write Feedback")

    st.text_area(f'#### Leave Feedback')

    st.form_submit_button('Submit Feedback')

Feedback_form()