import streamlit as st
import sys
sys.path.insert(1, 'controller')
import client as client

def home():
    st.title('Select All Person')

    rows = client.selectall()

    if rows:
        st.table(rows)
    else:
        st.write("No Data")

