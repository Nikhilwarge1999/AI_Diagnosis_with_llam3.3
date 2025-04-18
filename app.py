 
import streamlit as st
from login_page import show_login, show_register
from chat_history import ChatHistory
from model_load import generate_diagnosis_response

st.set_page_config(page_title="Medical Diagnosis Chatbot", page_icon="🧠", layout="centered")

# Session initialization
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Logout Button (if already logged in)
if st.session_state.authenticated:
    with st.sidebar:
        st.markdown("## 🔐 Account")
        if st.button("🚪 Logout"):
            st.session_state.authenticated = False
            st.rerun()

# If not authenticated, show login/register
if not st.session_state.authenticated:
    menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
    if menu == "Login":
        show_login()
    else:
        show_register()
    st.stop()

# Show chatbot UI
st.markdown("### 👨‍⚕️ Welcome to the AI Medical Diagnosis Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatHistory()

# Handle user input
user_input = st.chat_input("Describe your symptoms...")
if user_input:
    st.session_state.chat_history.add_user_message(user_input)
    with st.spinner("Analyzing symptoms..."):
        response = generate_diagnosis_response(user_input)
    st.session_state.chat_history.add_bot_message(response)

# Display chat history
for role, message in st.session_state.chat_history.get_all():
    with st.chat_message(role):
        st.markdown(message)
 
