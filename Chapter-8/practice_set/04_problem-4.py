# Q-4 Write a recursive function to calculate the sum of first n natural numbers.

"""
sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6
sum(4) = 1 + 2 + 3 + 4 = 10
sum(5) = 1 + 2 + 3 + 4 + 5 = 15

sum(n) = 1 + 2 + 3 + 4 + 5 + ... + n
sum(n) = n + sum(n - 1)
"""


def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


n = int(input("Enter a number: "))
print(f"Sum of {n} natural number is {sum(n)}")
