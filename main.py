todos = []
while True:
    user_action=input("add or show or exit:")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            user_text=input("Enter a todo:")
            todos.append(user_text)

        case 'show'|'display':
            for item in todos:
                item=item.title()
                print(item)
        case 'exit':
            break
        case whatever:
            print("Hyy,you entered the wrong command just enter the correct word")

print("byee")