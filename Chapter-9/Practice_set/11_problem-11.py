# Q-10 Write a python program to rename a file to “renamed_by_ python.txt.

with open("Chapter-9/Practice_set/old.txt", "r") as f:
    content = f.read()

with open("Chapter-9/Practice_set/renamed_by_ python.txt", "w") as f:
    f.write(content)
