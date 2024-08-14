import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)

st.title('My todo list')
st.subheader('Lets get to work')
st.write('This app is to increase my productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='-', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')

st.session_state

