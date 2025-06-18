import streamlit as st

def login_user():
    st.title("DockMate Login")
    role = st.selectbox("Login as", ["Boat Owner", "Vendor", "Marina Admin"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state["role"] = role
        st.session_state["username"] = username
        st.session_state["authenticated"] = True
        st.success(f"Logged in as {role}: {username}")
        st.switch_page("pages/dashboard.py")
