import streamlit as st
from modules import functions

todos = []
todos_list = functions.get_todos()
for i, item in enumerate(todos_list):
    todos_list[i] = item.title() + "\n"

def prepare_edit(todo_text):
    """Sets the text input value to the selected todo's text."""
    st.session_state["new_todo"] = todo_text.strip()

def add_todo():
    """Adds a new to-do item to the list and updates the text file."""
    todo = st.session_state["new_todo"]
    if todo:
        todos_list.append(todo.title() + "\n")
        functions.write_todos(todos_list)
        st.session_state["new_todo"] = ""

def edit_todo():
    """Removes a to-do item from the list and updates the text file."""
    new_text = st.session_state["new_todo"]
    for i,todo in enumerate(todos_list):
        # We check the session state of the existing checkbox keys
        if st.session_state.get(f"{todo}_{i}"):
            todos_list[i] = new_text.title() + "\n"
            functions.write_todos(todos_list)
            st.session_state["new_todo"] = ""
            break

def remove_todo():
    """Removes a to-do item from the list and updates the text file."""
    updated_list = [todo for i, todo in enumerate(todos_list)
                    if not st.session_state.get(f"{todo}_{i}")]
    functions.write_todos(updated_list)
    st.session_state["new_todo"] = ""


st.title("Welcome to My Todo App")
st.subheader("Add your tasks here:")
st.write("This is app is to help you manage your tasks.")

for i, todo in enumerate(todos_list):
    checkbox = st.checkbox(todo,
                           key=f"{todo}_{i}",
                           on_change=prepare_edit,
                           args=(todo,))

todo_input = st.text_input(label="Enter a new task:",
                           placeholder="Add a new task...",
                           key="new_todo")

# Action Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if todo_input:
        st.button(label="Add Task", on_click=add_todo)
    else:
        st.button(label="Add Task", disabled=True)
with col2:
    if todo_input:
        st.button(label="Edit Task", on_click=edit_todo)
    else:
        st.button(label="Edit Task", disabled=True)
with col3:
    if todo_input:
        st.button(label="Remove Task", on_click=remove_todo)
    else:
        st.button(label="Remove Task", disabled=True)

