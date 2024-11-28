# Q-4 write a python program to print conent of a directory  OS using moudle
# specify the directory you want to list
import os

directory = "/"

# list all the files in the directory
content = os.listdir(directory)

# pribt all the files and folders
for items in content:
    print(items)
