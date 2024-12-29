# Q-2 Write a class “Calculator” capable of finding square, cube and square root of a number.
import math

number = int(input("Enter a number: "))


class calculater:
    square = number * number
    print(f"Square of {number} number is {square}")

    cube = number * number * number
    print(f"Cube of {number} is {cube}")

    square_root = math.sqrt(number)
    print(f"Square root of {number} is {square_root}")
