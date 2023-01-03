import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo'] +'\n' # session state type: form of dict
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title('Vår huskeliste')
st.subheader('Blåbærveien 3')
st.write('Vollmo/Pallin')

st.text_input(label='', placeholder='Legg inn et gjøremål', 
on_change=add_todo, key='new_todo')





for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()




