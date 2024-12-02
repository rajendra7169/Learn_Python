"""
 snake, water gun game in python

    1 for snake
    -1 for water
    0 for gun
"""

# import random

# computer = random.choice([1, 0, -1])  # computer choice
# youstr = input("Enter your choice: snake, water, gun: ")
# youdict = {"s": 1, "w": -1, "g": 0}
# reversedict = {1: "snake", -1: "water", 0: "gun"}
# you = youdict[youstr]
# print(f"Computer chose {reversedict[computer]}\nYou chose {reversedict[you]}")
# if computer == you:
#     print("Tie")
# else:
#     if computer == 1 and you == -1:
#         print("You lose")
#     elif computer == -1 and you == 1:
#         print("You win")
#     elif computer == 1 and you == 0:
#         print("You win")
#     elif computer == 0 and you == 1:
#         print("You lose")
#     elif computer == 0 and you == -1:
#         print("You win")
#     elif computer == -1 and you == 0:
#         print("You lose")
#     else:
#         print("Invalid input")


# -------------------------------------OR--------------------------------------------

import random

computer = random.choice([1, -1, 0])

yourchoice = input("Enter your chice: ").lower()
youdict = {"s": 1, "w": -1, "g": 0}
revercedict = {1: "Snake", -1: "Water", 0: "Gun"}

if yourchoice not in youdict:
    print("Invalid Input. Chose between 's','w' and 'g'")

else:
    you = youdict[yourchoice]
    print(f"You chose {revercedict[you]}\nComputer chose {revercedict[computer]}")
    if computer == you:
        print("Tie")
    elif (
        (computer == 1 and you == -1)
        or (computer == 0 and you == 1)
        or (computer == -1 and you == 0)
    ):
        print("Computer Wins")

    else:
        print("You Win")
