# Q- 2 Write a python program using function to convert Celsius to Fahrenheit.


def temp():
    celsius = int(input("Enter temperature in celsius: "))
    fahrenhite = celsius * (9 / 5) + 32  # Here 9/5 = 1.8
    return fahrenhite


print(temp())


# function to convert Fahrenheit to Celsius:


def f_to_c():
    fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    celcious = (fahrenheit - 32) * 5 / 9
    return celcious


print(f_to_c())

# --------------------------------------------OR--------------------------------


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


fahrenheit = int(input("Enter temp in fahrenheit: "))
print(f"{fahrenheit}fahrenheit  to celcious is {f_to_c(fahrenheit)}")
