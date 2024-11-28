a = (1, 2, "Raja", 23.5, False, 5, 6, 2, 78.5, 2)
print(a)

no = a.count(2)  # It counts the number of value in atuple
print(no)

print(a.index(23.5))  # It show the posation of number in a tuple


# ---------- concatenation tuple

tuple1 = (
    1,
    7,
    68.9,
    444,
    "Raja",
    "Rohan",
    False,
)

tuple2 = (2, 6, 9, 45.5, "Puja", True, "Uma")

concatenated = tuple1 + tuple2
print(concatenated)  # Adds multiple tuples

multiply = tuple2 * 2
print(multiply)  # Multiply tuple

check = 2 in tuple2
print(check)  # Check if somthing is in a tuple in or not

print(len(tuple2))  # Provieds the lents of tuple

# print(min(tuple1))  # not supported between instances of 'str' and 'int'
