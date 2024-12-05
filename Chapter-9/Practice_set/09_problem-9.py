# Q-9 Write a program to find out whether a file is identical & matches the content of another file.

with open("Chapter-9/Practice_set/poem.txt", "r") as f:
    file1 = f.read()

with open("Chapter-9/Practice_set/poem_copy.txt", "r") as f:
    file2 = f.read()


if file1 == file2:
    print("Content matches.")
else:
    print("Content does not match.")
