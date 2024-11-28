# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, modulus, division,exponentiation etc.

add = 1+20

subtraction = 20-1

multiplication = 2*10

division = 20/2

modulus = 20 % 3

exponentiation = 2**3

print("1+20 = ", add, "\n20-1 = ", subtraction, "\n2*10 = ", multiplication,
      "\n20/2 = ", division, "\n20 % 3 = ", modulus, "\n2**3 = ", exponentiation)

# Assignment operators are used to assign values to variables.

y = 4-2  # assign 4-2 in a variable num
print(y)

x = 3  # initial value of x is 3
x += 2  # x = x+2 || which increse the value of x by 2
print(x)  # 3+2 = 5

p = 9  # initial value of p is 9
p -= 3  # p = p-3 || which decrease the value of p by 3
print(p)  # 9-3 = 6

q = 5  # initial value of q is 5
q *= 2  # q = q*2 || which multiply the value of q by 2
print(q)  # 5*2 = 10

r = 10  # initial value of r is 10
r /= 2  # r = r/2 || which divide the value of r by 2
print(r)  # 10/2 = 5

s = 10  # initial value of s is 10
s += 12 # s = s+12 || which increase the value of s by 12
s -= 2 # s = s-2 || which decrease the value of s by 2
s *= 2 # s = s*2 || which multiply the value of s by 2
s /= 2 # s = s/2 || which divide the value of s by 2
print(s)  # 10+12-2*2/2 = 20

# Comparison operators are used to compare two values.
value1 = 10
value2 = 20

print(value1 == value2) # False
print(value1 != value2) # True
print(value1 > value2) # False
print(value1 < value2) # True
print(value1 >= value2) # False
print(value1 <= value2) # True

# Logical operators are used to combine conditional statements.

e = True or False

# Truth table for OR operator
print("True or True = ", True or True)
print("True or False = ", True or False)
print("False or True = ", False or True)
print("False or False = ", False or False)

# Truth table for AND operator
print("True and True = ", True and True)
print("True and False = ", True and False)
print("False and True = ", False and True)
print("False and False = ", False and False)

# Truth table for NOT operator
print("not True = ", not True)
print("not False = ", not False)

