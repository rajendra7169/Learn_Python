# Q-6 Write a python function which converts inches to cms.


def inches_to_cm(inches):
    return inches * 2.4


inches = int(input("Enter the inches: "))
print(f"{inches} to cm is {inches_to_cm(inches)}")
