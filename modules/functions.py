import streamlit as st

#Variables
dir_name = "output"
file_name = "todos.txt"

#Define the file path depending on the module
if __name__ != "__main__":
    file_path = f"{dir_name}/{file_name}"
else:
    file_path = f"../{dir_name}/{file_name}"


# This function reads a text file and returns the list of to-do items.
def get_todos(filepath_l = file_path):
    """Reads a text file and returns the list of to-do items."""
    with open(filepath_l, "r") as file:
        todos_local = file.readlines()
    return [item.strip('\n') for item in todos_local]

# This function writes a list of to-do items into a text file.
def write_todos(todos_arg, filepath_l = file_path):
    """Writes a list of to-do items into a text file."""
    with open(filepath_l, "w") as file:
        file.writelines([item for item in todos_arg])

#If the program is run directly, it will print the to-do items.
if __name__ == "__main__":
    for index, item in enumerate(get_todos()):
        print(f"{index + 1} {'-'} {item.title()}")
#If the module is imported, it will print a success message.
else:
    print("Functions module imported successfully.")