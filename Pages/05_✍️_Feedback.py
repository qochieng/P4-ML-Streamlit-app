import streamlit as st
import pandas as pd 
import numpy as np
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_feedback import streamlit_feedback
# Initialize authentication_status if it's not already initialized
if 'authentication_status' not in st.session_state:
    st.session_state.authentication_status = False

# Check authentication status
if not st.session_state.authentication_status:
    st.info('Please Login to use Platform.')
    st.stop()


st.set_page_config(
    page_title = 'Feedback Page',
    layout = 'centered'
)
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

if 'authentication_status' in st.session_state:
    # path ="E:\AZUBI\DATA ANALYTICS\Analytics\PROJECTS\Project 4\P4-ML-Streamlit-app\Pages"
    # page_selection = st.sidebar.radio("Go to", ["Login","🏠Home","📋Data" ,"📊Dashboard", "📈Predict", "📚History"])

    # if page_selection == "Login.py":
    #     st.switch_page("Login.py")
    # elif page_selection == "🏠Home":
    #     st.switch_page("pages/00_🏠_Home.py")
    # elif page_selection == "📋Data":
    #     st.switch_page("pages/01_📋_Data.py")
    # elif page_selection == "📊Dashboard":
    #     st.switch_page("pages/02_📊_Dashboard.py")
    # elif page_selection == "📈Predict":
    #     st.switch_page("pages/03_📈_Predict.py")
    # elif page_selection == "📚History":
    #     st.switch_page("pages/04_📚_History.py")
    
    if st.sidebar.button('Logout',key='logout_button'):
        authenticator.logout()
        st.session_state["authentication_status"] = False
        #st.switch_page("Login.py")
#with st.form('Feedback Form'):
st.markdown('### Please enter Feedback or Questions')

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def display_answer():
    for i in st.session_state.chat_history:
        with st.chat_message("human"):
            st.write(i["question"])
        with st.chat_message("ai"):
            st.write(i["answer"])

        # If there is no feedback show N/A
        if "feedback" in i:
            st.write(f"Feedback: {i['feedback']}")
        else:
            st.write("Feedback: N/A")

def create_answer(question):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    message_id = len(st.session_state.chat_history)

    st.session_state.chat_history.append({
        "question": question,
        "answer": f"{question}_Answer",
        "message_id": message_id,
    })


def fbcb():
    message_id = len(st.session_state.chat_history) - 1
    if message_id >= 0:
        st.session_state.chat_history[message_id]["feedback"] = st.session_state.fb_k
    display_answer()


if question := st.chat_input(placeholder="Ask your question here .... !!!!"):
    create_answer(question)
    display_answer()

    ## thumbs up/down work with this approach 
    with st.form('form'):
        streamlit_feedback(feedback_type="thumbs", optional_text_label="[Optional]", align="flex-start", key='fb_k')
        st.form_submit_button('Save feedback', on_click=fbcb)

    ## thumbs up/down do NOT work with this approach 
    # streamlit_feedback(feedback_type="thumbs", optional_text_label="[Optional]",  align="flex-start", key='fb_k', on_submit='streamlit_feedback')
