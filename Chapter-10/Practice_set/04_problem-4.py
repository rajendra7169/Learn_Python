# Q-4 Add a static method in problem 2, to greet the user with hello.

import math

number = int(input("Enter a number: "))


class calculater:
    @staticmethod
    def greet():
        print("Hell0, Raja")

    square = number * number
    print(f"Square of {number} number is {square}")

    cube = number * number * number
    print(f"Cube of {number} is {cube}")

    square_root = math.sqrt(number)
    print(f"Square root of {number} is {square_root}")


# greeting = calculater()
# greeting.greet()

calculater.greet()
