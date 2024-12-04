# Q-8 Write a program to make a copy of a text file “this. txt”

with open("Chapter-9/Practice_set/poem.txt", "r") as f:
    content = f.read()

with open("Chapter-9/Practice_set/poem_copy.txt", "w") as f:
    f.write(content)

