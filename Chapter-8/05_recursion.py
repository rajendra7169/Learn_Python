"""
factorial(5) = 5*4*3*2*1
factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
factorial(2) = 2*1
factorial(1) = 1
factorial(0) = 1

factorial(n) = n * n-1* ....... 3*2*1

factorial(n) = n * factorial(n-1) 
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter a number: "))
print(f"The factorial of {n} = {factorial(n)}")


# How recursion works:
"""
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1

OR

factorial(5)
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1
"""

# Using for loop instant of funcation:
n = int(input("Enter a number: "))
result = 1

for i in range(1, n + 1):
    result *= i

print(f"The factorial of {n} = {result}")
