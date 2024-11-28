# Q-3 Can we have a set with 18 (int) and 18 (str) as a value in it?
# A-3 Yes, we can have a set with 18 (int) and 18 (str) as a value in it.
# Example:
set_num = set()
set_num.add(18)
set_num.add("18")
print(set_num)

# Method-2
set_num = set()
num1 = input("Enter the number : ")
set_num.add(int(num1))

num2 = input("Enter the string :")
set_num.add(num2)

print(set_num)
