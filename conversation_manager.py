import streamlit as st

def initialize_conversation():
    # Initialize conversation history in streamlit session state 
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_user_message(message):
    # add user message to conversation history
    
    st.session_state.chat_history.append({
        "role":"user",
        "content":message
    })
def add_assistant_message(message):
    # add assistant message to conversation history
    
    st.session_state.chat_history.append({
        "role":"assistant",
        "content":message
    })   
    
def get_conversation_history():
    # return conversation history
    
    return  st.session_state.chat_history
    
    
    
    
    