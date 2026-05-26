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


#users table

cursor_obj.execute("""
create table if not exists users(
               id int primary key auto_increment,
               name varchar(100),
               email varchar(100),
               password varchar(100)
               )
""")

# files table
cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS files (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    file_name VARCHAR(255),
    file_type VARCHAR(100),
    file_url TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
)
""")

conn_obj.commit()

print("tables created successfully")


