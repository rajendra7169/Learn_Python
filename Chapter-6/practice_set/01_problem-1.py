# Q-1 Write a prigram to find the greatest of four numbers entered by the user.
"""num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is the greatest")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} is the greatest")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num3} is the greatest")
else:
    print(f"{num4} is the greatest")"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

greatest = num1

if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4

print(f"The greatest number is {greatest}")
