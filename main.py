times=int(input("How many times do you want to enter To-Do's?"))

todos = []
for i in range(times):
    user_prompt="Enter To-Do:"
    user_text=input(user_prompt)
    todos.append(user_text)

print(todos)