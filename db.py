import streamlit as st
import mysql.connector

conn_obj=mysql.connector.connect(
    host=st.secrets["host"],
    database=st.secrets["database"],
    port=st.secrets["port"],
    user=st.secrets["user"],
    password=st.secrets["password"]
)

cursor_obj=conn_obj.cursor(dictionary=True)