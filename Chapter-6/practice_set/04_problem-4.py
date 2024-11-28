# Q-3 Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your UserName: ")

if len(username) >= 10:
    print("This username contains more than 10 chr.")

else:
    print("This username contains less than 10 chr.")
