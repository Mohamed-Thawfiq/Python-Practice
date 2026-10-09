password=input("Enter Password")

result={}

if len(password)>=8:
    result["lenght"]=True
else:
    result["lenght"]=False

digit=False

for i in password:
    if i.isdigit():
        digit=True

result["digits"]=digit

uppercase=False

for i in password:
    if i.isupper():
        uppercase=True

result["upper-case"]=uppercase

print(result.values()) #just to know what are the fields are true

if all(result.values()):
    print("Strong Password")
else:
    print("Week Password")