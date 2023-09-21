import streamlit as st
import page.insert as insert
import page.select as home
import page.update as update
import page.delete as delete

#สร้าง menu sidebar
st.sidebar.title('Menu')

page = st.sidebar.selectbox('',['Home','Insert', 'Update','Delete'])

#insert menu
if page=='Insert':
    insert.insert()
elif page=='Home':
    home.home()
elif page=='Update':
    update.update()
elif page=='Delete':
    delete.delete()


