# Q-5 Write a program to find whether a given name is presented in a list or not.

name = ["Raja", "Milan", "Roshan", "Kusum"]

enter_name = input("Enter your name: ")

if enter_name in name:
    print("Nmae is in list.")
else:
    print("Name not found.")
