import streamlit as st
from db import conn_obj,cursor_obj

st.title("Media Platform")

login,signup=st.tabs(
    ["Login","Sign up"]
    )


cursor_obj.execute("show databases")
dbs=cursor_obj.fetchall()

for db in dbs:
    st.wrute(db)


with signup:
    st.header("SignUp")
    with st.form("login_form"):
        name=st.text_input("name")
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        btn=st.form_submit_button("signup")

with login:
    st.header("Login")
    with st.form("login"):
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        btn=st.form_submit_button("Login")
