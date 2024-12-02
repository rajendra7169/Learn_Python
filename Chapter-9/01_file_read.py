# Open file in read mode and read the content of the file. Close the file after reading the content.
"""File I/O operation in Python:
1. Open file: open() function is used to open a file in Python.
2. Read file: read() function is used to read the content of the file.
3. Close file: close() function is used to close the file."""

"""Modes of opening a file in Python:
1. r: Open file in read mode.
2. w: Open file in write mode.
3. a: Open file in append mode.
4. r+: Open file in read and write mode.
5. w+: Open file in write and read mode.
6. a+: Open file in append and read mode."""


a = open("Chapter-9/file.txt")
b = a.read()
print(b)
a.close()
