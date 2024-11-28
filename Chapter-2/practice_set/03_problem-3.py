# Check the type of variable assigned using input() function.

user_input = input("Enter anything:")
int_user_input = int(input("Enter a number:"))

print(type(user_input))
print(type(int_user_input))

# OR

user2_input = input("Enter anything:")
int_user2_input = int(input("Enter a number"))

x = type(user2_input)
y = type(int_user2_input)

print("This is:", x)
print("this is:", y)
