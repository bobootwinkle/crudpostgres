import streamlit as st
import sys
sys.path.insert(1, 'controller')
import client as client

def insert():
    st.title('Insert Person')

    #สร้าง form
    with st.form(key="insert"):
        input_full_name = st.text_input("Fullname")
        input_email = st.text_input("Email")
        input_age = st.number_input("Age",1,100,1)
        btn_submit = st.form_submit_button("Submit")

        #check ถ้าปุ่มโดนกด
        if btn_submit:
            client.insert(input_full_name, input_email, input_age)
            st.success("Insert Person Success")