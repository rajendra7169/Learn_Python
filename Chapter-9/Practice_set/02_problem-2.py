# Q-2 The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random


def game():
    # Generate a random score between 1 and 100
    score = random.randint(1, 100)
    return score


# Play the game and get the score
result = game()
print(f"Your score: {result}")

file_path = "Chapter-9/Practice_set/high_score.txt"

# Read the current high score from the file
with open(file_path, "r") as f:
    read = f.read().strip()

# Check if there is a valid score in the file
if read:
    high_score = int(read)
else:
    high_score = 0  # If the file is empty, set the high score to 0

print(f"Previous high score: {high_score}")

# Compare the current result with the high score and update if necessary
if result > high_score:
    print("Congratulations! You set a new high score!")
    with open(file_path, "w") as f:
        f.write(str(result))  # Write the new high score
else:
    print("Try again to beat the high score!")
