# Q-4 What will be the length of the following set S:
"""
S = set()
S.add(20)
S.add(20.0)
S.add("20") 
"""
S = set()
S.add(20)
S.add(20.0)
S.add("20")
print(len(S))  # Output: 2 because 20 and 20.0 are same in set.

# And

S = set()
S.add(20)
S.add(20.2)
S.add("20")
print(len(S))  # Output: 3 because 20, 20.2 and "20" are different in set.
