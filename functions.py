FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Retrives the content of the file specified as a todos list """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos( todos_arg, filepath=FILEPATH):
    """ Overwrites the file with the fist argument """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print('Functions initialised')
    print(get_todos())