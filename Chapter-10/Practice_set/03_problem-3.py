# Q-3 Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?


class Demo:
    a = 10


b = Demo()
b.a = 0
print(b.a)
print(Demo.a)  # No, it does not change the class attribute.
