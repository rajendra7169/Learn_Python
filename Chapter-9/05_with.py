a = open("Chapter-9/file.txt")
b = a.read()
print(b)
a.close()

# The same code can be written using with statement as shown below:
with open("Chapter-9/file.txt") as f:
    print(f.read())

# The with statement is used to wrap the execution of a block of code. This ensures that the file is closed when the block of code is exited.
