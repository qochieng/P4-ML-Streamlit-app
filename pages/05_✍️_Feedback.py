import streamlit as st
import pandas as pd 
import numpy as np
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_feedback import streamlit_feedback
# Initialize authentication_status if it's not already initialized
from Login import login


st.set_page_config(
    page_title = 'Feedback Page',
    layout = 'centered'
)


def feed():
   
    login()
    if st.session_state["authentication_status"] is True:
    
       
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
if __name__ == "__main__":
    feed()