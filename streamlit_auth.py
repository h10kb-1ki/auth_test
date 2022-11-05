import streamlit as st
from time import sleep

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("テストページです")
    btm = st.button("Click me")
    if btm:
        st.markdown("""
        <style>
        .stProgress .st-bo {
            background-color: green;
        }
        </style>
        """, 
        unsafe_allow_html=True)

        progress = st.progress(0)

        for i in range(20):
            progress.progress(i)
            sleep(0.1)
    