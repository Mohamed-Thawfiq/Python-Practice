todos = []
while True:
    user_action=input("add or show or exit:")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            user_text=input("Enter a todo:")
            todos.append(user_text)

        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print("byee")