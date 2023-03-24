# from function import get_todos, write_todos
from modules import function
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = function.get_todos()

        todos.append(todo + '\n')

        function.write_todos(todos)

    elif user_action.startswith('show'):
        todos = function.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = function.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            function.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = function.get_todos()

            number = number - 1
            todo_to_remove = todos[number].strip("\n")
            new_todo = todos.pop(number)

            function.write_todos(todos)

            message = f"Todo {todo_to_remove.upper()} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("bye")
