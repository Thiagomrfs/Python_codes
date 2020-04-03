

# PYTHON 3

name = input("write your name: ") # if you don't specify a type python will use str
father = input("write your father's name: ")
age = int(input("write your age: "))
status = ""

if age <= 10:
    status = "a child"
elif 10 < age <= 20:
    status = "a teen"
elif 20 < age <= 30:
    status = "an adult"
else:
    status = "older than a thought"

print(f"""
Your name is {name}
Your father's name is {father}
You are {age} years old!

Based on your age you are {status}!
""")
