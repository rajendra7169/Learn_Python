s1 = {1, 45, 6, 99, 86, "Raja"}
s2 = {2, 6, 75, "Raja", 28, 99}

print(s2.union(s1))  # Prints all values from s1 and s2 without reapting the value

# print(s1.union(s2))

print(s1.intersection(s2))  # Prints common values form both sets

#  --------OR

print(s1 & s2)  # Another method to  use intersection

# To find unique value
print(s1 - s2)

# Define empty set and add values on it
unique_visiter = set()

# Add visiters IDs
unique_visiter.add("visiter1")
unique_visiter.add("visiter2")
unique_visiter.add("visiter1")  # Duplicate will not be added

print(unique_visiter)
print(len(unique_visiter))  # Prints the lenth of unique visiters
