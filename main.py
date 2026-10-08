while True:
    user_action=input("add or show or edit or exit:")
    user_action=user_action.strip()
    if 'add' in user_action:
        user_text=user_action[4:]

        # file=open('todos.txt','r')
        # todos=file.readlines()
        # file.close()

        with open('todos.txt','r') as file:
            todos=file.readlines()
            
        todos.append(user_text)
        # file=open('todos.txt','w')
        # file.writelines(todos)
        # file.close()

        with open('todos.txt','w') as file:
            file.writelines(todos)


    if 'show' in user_action or 'display' in user_action:
        # file=open('todos.txt','r')
        # todos=file.readlines()
        # file.close()

        with open('todos.txt','r') as file:
            todos=file.readlines()

        for index, item in enumerate(todos):
            item=item.title()
            print(f"{index+1}.{item}")

    # case 'edit':
    #     number=int(input("Enter the number of the todo to edit:"))
    #     number=number-1
    #     new_todo=input("Enter the new todo:")
    #     todos[number]=new_todo
    #     with open('todos.txt','w') as file:
    #         file.writelines(todos)

    if 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)
    if 'complete' in user_action:
        number=int(input("Enter the number of the todo to complete:"))
        todos.pop(number-1)
    if 'exit' in user_action:
        break
    if 'whatever' in user_action:
        print("Hyy,you entered the wrong command just enter the correct word")

print("byee")






content=['mohamed','thowfik','ahmed']
filenames=['file1.txt','file2.txt','file3.txt']
for content,filename in zip(content,filenames):
    file=open(f"{filename}","w")
    file.write(content)
    file.close()