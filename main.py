todos = ''

user_prompt = 'Enter a to do: '

flag = True

while flag:
    todo = input(user_prompt)
    todos = todos + '\n' + todo
    flag1 = True
    while flag1:
        Continue = input('Do you want to add another to do? [y/n]: ').lower()
        if Continue != 'y' | 'n':
            print('Please enter y or n')
        elif Continue == 'y':
            flag1 = False
        elif Continue == 'n':
            print("That's all. Here is your to do list:", todos)
            flag1 = False
            flag = False
