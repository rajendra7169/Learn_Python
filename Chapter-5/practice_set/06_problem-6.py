# Q-6 Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.

fav_lang = {}
name1 = input("Enter your name : ")
lang1 = input("Enter your favorite language : ")

name2 = input("Enter your name : ")
lang2 = input("Enter your favorite language : ")

name3 = input("Enter your name : ")
lang3 = input("Enter your favorite language : ")

name4 = input("Enter your name : ")
lang4 = input("Enter your favorite language : ")

fav_lang[name1] = lang1
fav_lang[name2] = lang2
fav_lang[name3] = lang3
fav_lang[name4] = lang4

print(fav_lang)
print(type(fav_lang))

# Another way to solve this problem:

d = {}
name = input("Enter your name : ")
lang = input("Enter your favorite language : ")
d.update({name: lang})

name = input("Enter your name : ")
lang = input("Enter your favorite language : ")
d.update({name: lang})

name = input("Enter your name : ")
lang = input("Enter your favorite language : ")
d.update({name: lang})

name = input("Enter your name : ")
lang = input("Enter your favorite language : ")
d.update({name: lang})

print(d)

# The second program is generally more Pythonic and efficient because it uses update() and reuses variables. However, in both cases, a loop would make the code cleaner and more scalable.
