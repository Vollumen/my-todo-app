import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo'] +'\n' # session state type: form of dict
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title('Min Todo-App')
st.subheader('Min første web-app')
st.write('Økt produktivitet - Bedre kompetanse i Python')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Legg inn et gjøremål', 
on_change=add_todo, key='new_todo')


st.session_state