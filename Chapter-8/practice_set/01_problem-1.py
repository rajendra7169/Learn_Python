# Q-1 Write a program using functions to find greatest of three numbers.
def greatest_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    greatest = num1
    if num2 > greatest:
        greatest = num2
    if num3 > greatest:
        greatest = num3

    return greatest


print(greatest_num())
