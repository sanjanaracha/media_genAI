import streamlit as st
from db import conn_obj,cursor_obj

st.title("Media Platform")

login,signup=st.tabs(
    ["Login","Sign up"]
    )


cursor_obj.execute("show databases")
dbs=cursor_obj.fetchall()

for db in dbs:
    st.write(db)

cursor_obj.execute("show tables")
tables=cursor_obj.fetchall()

for db in tables:
    st.write(db)


with signup:
    st.header("SignUp")
    with st.form("login_form"):
        name=st.text_input("name")
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        btn=st.form_submit_button("signup")

        if btn:
            qurey="insert into users(name,email,password)values(%s,%s,%s)"
            values=(name,email,password)
            cursor_obj.execute(qurey,values)
            conn_obj.commit()
            st.write("user added successfully")



with login:
    st.header("Login")
    with st.form("login"):
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        btn=st.form_submit_button("Login")
