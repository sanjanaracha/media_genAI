import streamlit as st
from db import conn_obj,cursor_obj

import cloudinary
import cloudinary.uploader
#pip install cloudinary 


st.title("Media Platform")

cloudinary.config(
    cloud_name=st.secrets["cloud_name"],
    api_key=st.secrets["api_key"],
    api_secret=st.secrets["api_secret"]
)

if "user" not in st.session_state:
    st.session_state.user=None



# cursor_obj.execute("show databases")
# dbs=cursor_obj.fetchall()

# for db in dbs:
#     st.write(db)

# cursor_obj.execute("show tables")
# tables=cursor_obj.fetchall()

# for db in tables:
#     st.write(db)


def dashboard():
    st.sidebar.success("welcome user")
    st.header("dashboard")

    opt=st.sidebar.selectbox("choose:--",["uploadFiles","ViewFiles","Logout"])

    if opt=="uploadFiles":
        st.header("upload your files here")
        choosedfile=st.file_uploader("choose file",type=["pdf","jpg","jpeg","png","mp3","mp4"])
        if choosedfile:
            st.write(choosedfile.name)
            st.write(choosedfile.type)
        if "image" in choosedfile.type:
            st.image(choosedfile)
        elif "video" in choosedfile.type:
            st.video(choosedfile)
        elif "audio" in choosedfile.type:
            st.audio(choosedfile)

        if st.button("upload file to cloudinary"):
            uploded_dict_obj=cloudinary.uploader.upload(choosedfile,resource_type="auto")
            url=uploded_dict_obj["secure_url"]
            st.write(url)
            st.write("file uploded to cloudinary")

    elif opt=="Logout":
        st.session_state.user=None
        st.success("logout success")
        st.rerun() 





def signup_fun():
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



def login_fun():
    st.header("Login")
    with st.form("login"):
        email=st.text_input("email")
        password=st.text_input("password",type="password")
        btn=st.form_submit_button("Login")

        if btn:
            qurey="select * from users where email=%s and password=%s"
            values=(email,password)
            cursor_obj.execute(qurey,values)
            loggedin_user=cursor_obj.fetchone()
            st.session_state.user=loggedin_user
            st.write("loggedin successfully")
            st.rerun()



if st.session_state.user==None:
    login,signup=st.tabs(
    ["Login","Sign up"]
    )
    with signup:
        signup_fun()
    with login:
        login_fun()

else:
    dashboard()
