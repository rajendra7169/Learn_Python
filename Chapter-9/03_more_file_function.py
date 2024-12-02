# This program is used to read the file using readlines() and readline() function:

f = open(
    "Chapter-9/read_file.txt"
)  # open() function is used to open the file in read mode. If the file is not present, it will throw an error.

# lines = (
#     f.readlines()
# )  # readlines() function is used to read the file line by line and return the list of lines.
# print(lines, type(lines))

# Note: readline() and readlines() function cant be used together. If you use both, the second function will not work.

line1 = (
    f.readline()
)  # readline() function is used to read the file line by line and return the line.
print(line1, type(line1))

line2 = f.readline()
print(
    line2,
)

line3 = f.readline()
print(
    line2,
)

f.close()


# -------------------------Or-------------------------#
# Using while loop to read the file line by line:

g = open("Chapter-9/read_file.txt")

while True:
    line = g.readline()
    if not line:
        break
    print(line, end="")
g.close()
