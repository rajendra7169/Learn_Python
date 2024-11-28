friends = ["Raja", "Rohan", 23, 12, False, "Jessica", 464.56]
print(friends)

friends.append("Puja")  # Append adds somthing at last
print(friends)

list1 = [2, 5, 8, 9, 3, 6, 1, 4, 7, 10]
list1.sort()
print(list1)

list1.reverse()
print(list1)


list2 = [2, 5, 8, 9, 3, 6, 1, 4, 7, 10]
list2.sort()
list2.pop(9)
print(list2)
print(list2.pop(3))

result = list2.pop(6)
print(result)

list2.insert(6, "Raja")  # Insert "Raja" at the 6th position in the list
print(list2)

list2.remove(7)
print(list2)
