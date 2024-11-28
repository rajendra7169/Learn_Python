# Q-1 Write a program to create a dictionary of Nepali words with values as their English translation. Provides user with an option to look ot up.

nepali_words = {
    "Amma": "Mother",
    "Buba": "Dad",
    "Hajuraama": "Grandmother",
    "Hajurbuba": "Grandfather",
    "Kaka": "Uncle",
}

lookup = input("Enter desire Nepali Word to translate: ")
print(nepali_words[lookup])
print(nepali_words)
