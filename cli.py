import functions
import time

now = time.strftime('%d %b %Y, %X')
print('Today is', now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for i, item in enumerate(todos):
            row = f"{i+1}. {item}"
            row = row.strip()
            print(row)
        print(f"You have {len(todos)} tasks to do")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            print('\n', number + 1)

            with open('todos', 'r+') as file:
                todos = file.readlines()

            print(todos[number])
            new_todo = input('Write new todo instead of existing one: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Please enter a number!')
            continue

        print(f'\nYou edited {number+1} to do:\n{todos[number]}')
    #     Add functionality to complete multiple tasks, last task and first task
    elif user_action.startswith('complete'):
        try:
            number = int(input('Enter a number of todo completed: '))

            with open('todos', 'r+') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
        except IndexError:
            print('There is no number with that number!')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Please enter a correct command :)')

print('Bye!')
