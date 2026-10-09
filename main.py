from django.core.handlers import exception


while True:
    user_action=input("add or show or edit or complete or exit:")
    user_action=user_action.strip()
    if 'add' in user_action:
        try:
            user_text=user_action[4:]+'\n'

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
        except Exception as e:  
            print("An error occurred while trying to add the todo:", str(e))

    elif 'show' in user_action or 'display' in user_action:
        # file=open('todos.txt','r')
        # todos=file.readlines()
        # file.close()
        try:
            with open('todos.txt','r') as file:
                todos=file.readlines()

            for index, item in enumerate(todos):
                item=item.title()
                print(f"{index+1}.{item}")

        except Exception as e:
            print("An error occurred while trying to show the todos:", str(e))

    # case 'edit':
    #     number=int(input("Enter the number of the todo to edit:"))
    #     number=number-1
    #     new_todo=input("Enter the new todo:")
    #     todos[number]=new_todo
    #     with open('todos.txt','w') as file:
    #         file.writelines(todos)

    elif 'edit' in user_action:
        try:        
            number = int(user_action[5:])
            print("You are editing the todo number:",number)
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except Exception as e:
            print("An error occurred while trying to edit the todo:", str(e))
    elif 'complete' in user_action:
        try:
            task=int(user_action[9:])   
            with open('todos.txt','r') as file:
                todos=file.readlines()
            todos.pop(task-1)
            with open('todos.txt','w') as file:
                file.writelines(todos)
        except Exception as e:
            print("You entered an invalid number, please try again.")
    elif 'exit' in user_action:
        try:
            break
        except Exception as e:
            print("An error occurred while trying to exit the program:", str(e))
    else:
        print("Hyy,you entered the wrong command just enter the correct word")

print("byee")





# {seprate


content=['mohamed','thowfik','ahmed']
filenames=['file1.txt','file2.txt','file3.txt']
for content,filename in zip(content,filenames):
    file=open(f"{filename}","w")
    file.write(content)
    file.close()


# till here}