# Q-3 A spam comment is defined as a text containing the following keywords: "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("Enter your comment: ")

if (p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment):
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")

# ________________ 0R _______________________

comment2 = input("Enter your comment: ")

if (
    ("make a lot of money" in comment2)
    or ("buy now" in comment2)
    or ("subscribe this" in comment2)
    or ("click this" in comment2)
):
    print("This is a spam.")

else:
    ("This is not a spam")

# ________________ 0R _______________________

message = input("Enter your message: ")

if "make a lot of money" in message:
    print("This is a spam.")
elif "buy now" in message:
    print("This is a spam.")
elif "subscribe this" in message:
    print("This is a spam.")
elif "click this" in message:
    print("This is a spam.")
else:
    print("This is not a spam.")
