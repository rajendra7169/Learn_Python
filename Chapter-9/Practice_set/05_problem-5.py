# Q-5 Repeat program 4 for a list of such words to be censored.

words = ["donkey", "animal", "strong", "life"]

with open("Chapter-9/Practice_set/Donkey_2.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("Chapter-9/Practice_set/Donkey_2.txt", "w") as f:
    f.write(content)
