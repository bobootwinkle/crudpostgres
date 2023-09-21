import streamlit as st
import sys
sys.path.insert(1, 'controller')
import client as client

def delete():
    st.title('Delete Person Information')

    update_id = st.number_input("Input ID",format="%d",step=1)
    if st.button('Delete'):
        client.deletebyid(update_id)
        st.success('Delete Success')