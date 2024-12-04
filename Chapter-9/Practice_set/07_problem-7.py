# Q-7 Write a program to find out the line number where python is present from ques 6.


with open("Chapter-9/Practice_set/Log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
found = False
for line in lines:
    # Explicitly check if "Python" exists in the line
    if "Python" in line:
        print(f"Yes! Python is available in line {lineno}")
        found = True
    lineno += 1

if not found:
    print("No! Python is not present in any line.")
