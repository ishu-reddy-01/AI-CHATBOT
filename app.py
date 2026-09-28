import streamlit as st
import ollama
st.title("AI CHATBOT")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
user_input=st.chat_input("Type your message...")
if user_input:
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })
    with st.chat_message("user"):
        st.write(user_input)
    response=ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )
    bot_response=response["message"]["content"]
    st.session_state.messages.append({
        "role":"assistant",
        "content":bot_response
    })
    with st.chat_message("assistant"):
        st.write(bot_response)