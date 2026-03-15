import streamlit as st
from conversation_manager import initialize_conversation , add_user_message , add_assistant_message , get_conversation_history
from memory_extractor import extract_user_facts
from memory_manager import update_memory
from llm import generate_response
from memory_extractor import extract_user_facts
from memory_manager import update_memory
from memory_reasoner import should_store_fact
from memory_manager import get_memory
from memory_manager import save_memory
import json


st.title("personal AI assistant")

initialize_conversation()

user_input = st.chat_input("Ask something ...")

if user_input:

    add_user_message(user_input)

    # extract memory
    facts = extract_user_facts(user_input)
    if facts:
        update_memory(facts)

    history = get_conversation_history()

    response = generate_response(user_input, history)

    add_assistant_message(response)

for msg in st.session_state.chat_history:

    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])

    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])
        
facts = extract_user_facts(user_input)

if facts:

    decisions = should_store_fact(facts)

    filtered_facts = {}

    for key, decision in decisions.items():

        if decision in ["store", "update"]:
            filtered_facts[key] = facts[key]

    if filtered_facts:
        update_memory(filtered_facts)
    
with st.sidebar:

    st.header("User Profile")

    memory = get_memory()

    if memory.get("name"):
        st.write("Name:", memory["name"])

    if memory.get("goals"):
        st.write("Goals:", ", ".join(memory["goals"]))

    prefs = memory.get("preferences", {})

    if prefs.get("programming_languages"):
        st.write(
            "Preferred Languages:",
            ", ".join(prefs["programming_languages"])
        )

    if prefs.get("topics"):
        st.write(
            "Interested Topics:",
            ", ".join(prefs["topics"])
        ) 
        
    if st.button("Reset Memory"):

        empty_memory = {
            "name": None,
            "goals": [],
            "preferences": {
                "programming_languages": [],
                "topics": []
            }
        }

        save_memory(empty_memory)

        st.success("Memory cleared. Restart chat.")
        
    if "chat_history" in st.session_state:

        conversation_data = json.dumps(
            st.session_state.chat_history,
            indent=2
        )

        st.download_button(
            label="Download Conversation",
            data=conversation_data,
            file_name="conversation.json",
            mime="application/json"
        )
