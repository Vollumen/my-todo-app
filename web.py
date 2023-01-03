import streamlit as st
import functions

todos = functions.get_todos()

st.title('Min Todo-App')
st.subheader('Min første web-app')
st.write('Økt produktivitet - Bedre kompetanse i Python')

for todo in todos:
    st.checkbox(todo)

st.text_input('', placeholder='Legg inn et gjøremål')