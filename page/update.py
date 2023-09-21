import streamlit as st
import sys
sys.path.insert(1, 'controller')
import client as client

def update():
    st.title('Update Person Information')
    update_id = st.number_input("Input ID",format="%d",step=1)
    input_fullname = st.text_input("Fullname")
    input_email = st.text_input("Email")
    input_age = st.number_input("Age")

    #check ปุ่มว่ากดยัง
    if st.button('Update'):
        

        client.updatebyid(update_id,input_fullname,input_email,input_age)
        st.success("Update Person Success")
        
        
        