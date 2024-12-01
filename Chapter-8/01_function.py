# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# average = (a + b + c) / 3
# print(average)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# average = (a + b + c) / 3
# print(average)

# ----------------------------------------------------------------------------

# We can do this using function in a esay and short way.

"""
There are two type of function: 1. Builtin (Predefined) function and 2. Userdefined (custom) functions.
example:
Builtin (Predefined) function:
1. print()  # Builtin function
2. sum()  # Builtin function
3. input()  # Builtin function
4. int()  # Builtin function
5. float()  # Builtin function

Userdefined function:
1. def function_name():  # Function definition
    # Body of function
    # Code
    # Code
    # Code

"""


# Without passing argument:
def avg():  # Function definition
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    avgrage = (a + b + c) / 3
    print(avgrage)


avg()  # Function call
print("Thank you!")
avg()
avg()
print("Thank you!")
avg()

# ---------------------OR----------------------------


# Another method by passing an argument:
def addtion(num1, num2, num3):
    print(f"Avrage of three number is: {(num1+num2+num3)/3}")


addtion(2, 3, 4)
addtion(5, 7, 9)
addtion(1, 2, 3)

# -------------------------------------------------------


def greeting():
    username = input("Ehter your name: ")
    print(f"Hello 🙋‍♂️ {username}")  # print("Hello 🙋‍♂️", username)


greeting()

# ---------------------------------------------------------------


def greet(name):
    print(f"hello {name}")


greet(input("Enter your name: "))
