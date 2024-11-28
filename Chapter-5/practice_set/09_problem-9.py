# Q-9 Can you change the values inside a list which is contained in set s?
# s = {8, 7, 12, "Harry", [1, 2]}

s = {
    8,
    7,
    12,
    "Harry",
    [1, 2],
}  # First of all list can not be placed inside a set. So, the TypeError will be raised.

s.update([1, 2, 3, 4, 5])
print(s)  # Output: TypeError: unhashable type: 'list'

# Answer: No, we can't change the values inside a list which is contained in set s. Because the list is unhashable type. The set contains only hashable type of values. The list is unhashable type of value. So, we can't change the values inside a list which is contained in set s. The TypeError will be raised.

"""
Note: 
Hashable objects: These have a fixed hash value and can be used as keys in dictionaries or stored in sets (e.g., integers, strings, tuples).

Unhashable objects: These do not have a fixed hash value and cannot be used as keys. Examples include lists, dictionaries, or sets, which are mutable (their contents can change).
"""
