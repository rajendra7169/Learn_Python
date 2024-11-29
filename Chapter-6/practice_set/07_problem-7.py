# Q-7 Write a program to find out whether a given post is talking about “Harry” or not.

keyword = "Raja"

post = input("Enter your post: ")

if keyword.lower() in post.lower():
    print("This post is talking about Raja.")
else:
    print("This post is not about Raja")
