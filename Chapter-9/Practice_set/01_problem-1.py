# Q-1 Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

poems = open("Chapter-9/Practice_set/poem.txt")
read_poems = poems.read()

if "twinkle" or "Twinkle" in read_poems:
    print("There is twinkle word in the poems.")
else:
    print("There is not twinkle word in the poems.")

poems.close()
