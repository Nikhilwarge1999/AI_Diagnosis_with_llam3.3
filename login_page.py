import streamlit as st
from auth import login_user, register_user, reset_password
import time

def show_login():
    st.title("🔐 Login")

    if "reset_mode" not in st.session_state:
        st.session_state.reset_mode = False

    email = st.text_input("Email")

    # Show password input only if not in reset mode
    if not st.session_state.reset_mode:
        password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if not st.session_state.reset_mode:
            if st.button("Login"):
                success, result = login_user(email, password)
                if success:
                    st.session_state.authenticated = True
                    st.session_state.user_name = result.get("name", "")
                    st.success("Logged in successfully!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please try again.")

        else:
            if st.button("Send Reset Link"):
                reset_success = reset_password(email)
                if reset_success:
                    st.success("Reset link sent to your email.")
                    st.session_state.reset_mode = False
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Failed to send reset link. Try again.")

    with col2:
        if st.button("Forgot Password?" if not st.session_state.reset_mode else "Back to Login"):
            st.session_state.reset_mode = not st.session_state.reset_mode
            st.rerun()


def show_register():
    st.title("📝 Register")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        success, result = register_user(email, password, name)
        if success:
            st.success(result)
        else:
            st.error(result)
