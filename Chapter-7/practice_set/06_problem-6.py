# Q-6 Write a program to calculate the factorial of a given number using for loop.
# factorial(!): 5! = 1*2*3*4*5

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i

print(f"The factorial of {num} = {fact}")
