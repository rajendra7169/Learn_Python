# Q-1  Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter number: "))

i = 0
sum = 0

while i <= num:
    sum += i  # sum = sum+i
    i += 1  # i = i +1
print(sum)
