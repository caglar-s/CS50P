"""
In a file called camel.py, implement a program that prompts the user for the name of a 
variable in camel case and outputs the corresponding name in snake case. Assume that the user’s 
input will indeed be in camel case.
"""


user_input = input("camelCase: ")

for c in user_input:
    if c.isupper():
        print("_" + c.lower(),end = "")
    else:
        print(c,end = "")
print()
