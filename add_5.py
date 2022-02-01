#I used https://www.delftstack.com/howto/python/user-input-int-python/
#to find the isnumeric method that determines wether or not a number is an int

#Takes 5 numbers from the user and adds them together
num1 = input("Enter int #1: ")

#sees if the user entered an int and if not keeps prompting the user until they do
if not num1.isnumeric():
    while not num1.isnumeric():
        print("Please enter an int.")
        num1 = input("Enter int #1: ")
num1 = int(num1)

num2 = input("Enter int #2: ")

#sees if the user entered an int and if not keeps prompting the user until they do
if not num2.isnumeric():
    while not num2.isnumeric():
        print("Please enter an int.")
        num2 = input("Enter int #2: ")
num2 = int(num2)

num3 = input("Enter int #3: ")

#sees if the user entered an int and if not keeps prompting the user until they do
if not num3.isnumeric():
    while not num3.isnumeric():
        print("Please enter an int.")
        num3 = input("Enter int #3: ")
num3 = int(num3)
    
num4 = input("Enter int #4: ")

#sees if the user entered an int and if not keeps prompting the user until they do
if not num4.isnumeric():
    while not num4.isnumeric():
        print("Please enter an int.")
        num4 = input("Enter int #4: ")
num4 = int(num4)
    
num5 = input("Enter int #5: ")

#sees if the user entered an int and if not keeps prompting the user until they do
if not num5.isnumeric():
    while not num5.isnumeric():
        print("Please enter an int.")
        num5 = input("Enter int #5: ")
num5 = int(num5)

#prints the result
print(num1 + num2 + num3 + num4 + num5)
    