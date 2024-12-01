# Q-7 Write a python function to remove a given word from a list and strip it at the same time.


def rem(list, word):
    n = []
    for items in list:
        if not (items == word):
            n.append(items.strip(word))
    return n


list = ["Raja", "Milan", "Rohan", "Shunil", "Rojan"]
print(rem(list, "an"))
