todos = []
while True:
    user_action=input("add or show or exit:")
    match user_action:
        case 'add':
            user_text=input("Enter a todo:")
            todos.append(user_text)

        case 'show':
            print(todos)
        case 'exit':
            break

print("byee")