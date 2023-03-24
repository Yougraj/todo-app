




def get_todos(filepath='todo-app/todo.txt'):
    """Return the todo list in the todo.txt file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todo_arg ,filepath='todo-app/todo.txt'):
    """ Write the todo items list in the text file"""

    with open(filepath, "w") as file:
        file.writelines(todo_arg)
        




# print(help(get_todos))
# this is a doc string 