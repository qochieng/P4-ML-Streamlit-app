import streamlit as st
import pandas as pd 
import numpy as np


st.set_page_config(
    page_title = 'Feedback Page',
    layout = 'centered'
)


def feedback_form():

   with st.form('Feedback Form'):
   


    st.markdown(f"## Write Feedback")

    st.text_area(f'#### Leave Feedback')

#     elements = st.container()
# >>> elements.line_chart(...)

#     st.write("Hello")
#     elements.text_input()

    st.form_submit_button('Submit Feedback')
    Contact = "https://github.com/qochieng/P4-ML-Streamlit-app"

    st.markdown(f"For more Information Contact us at {Contact}", unsafe_allow_html=True)




feedback_form()
