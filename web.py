import streamlit as st
import functions

todos = functions.get_todos()

st.title('My todo list')
st.subheader('Lets get to work')
st.write('This app is to increase my productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add new todo...')

