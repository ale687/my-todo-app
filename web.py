import streamlit as st
import funciones

todos = funciones.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    if todo.strip():
        todos.append(todo)
        funciones.write_todos(todos)
        st.session_state["new_todo"] = ""



st.title("Mi Lista de Tareas")
st.subheader("Esta es mi app de lista de tareas")
st.write("Esta app incrementa mi productividad")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        funciones.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()                                        
    
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

