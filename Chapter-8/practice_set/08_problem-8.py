# Q-8 Write a python function to print multiplication table of a given number.


def multipy(num):
    for i in range(1, 11):
        print(num * i)


num = int(input("Enter a number: "))
print(multipy(num))
