while True:
    user_action=input("add or show or edit or exit:")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            user_text=input("Enter a todo:")+"\n"

            file=open('todos.txt','r')
            todos=file.readlines()
            file.close()
            todos.append(user_text)
            file=open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show'|'display':
            for index, item in enumerate(todos):
                item=item.title()
                print(f"{index+1}.{item}")
        case 'edit':
            number=int(input("Enter the number of the todo to edit:"))
            number=number-1
            new_todo=input("Enter the new todo:")
            todos[number]=new_todo

        case 'complete':
            number=int(input("Enter the number of the todo to complete:"))
            todos.pop(number-1)
        case 'exit':
            break
        case whatever:
            print("Hyy,you entered the wrong command just enter the correct word")

print("byee")