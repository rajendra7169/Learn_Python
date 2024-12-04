# Q-4 A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
word = "Donkey"

with open("Chapter-9/Practice_set/Donkey.txt", "r") as f:
    content = f.read()

content_new = content.replace(word.lower(), "######")

with open("Chapter-9/Practice_set/Donkey.txt", "w") as f:
    f.write(content_new)
