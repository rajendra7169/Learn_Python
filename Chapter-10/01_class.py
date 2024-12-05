# Defining a class in Python. A class is a blueprint for creating objects. It defines a set of attributes that will characterize any object that is instantiated from this class. Attributes are data members (class variables and instance variables) and methods, accessed via dot notation. A class is a logical entity that has some attributes and methods.


class employee:
    language = "Python"  # This is a class variable, it is shared by all instances of the class.
    salary = 120000


raja = employee()
raja.name = (
    "Raja"  # This is an instance attribute, it is unique to each instance of the class.
)
print(raja.name, raja.salary, raja.language)

milan = employee()
milan.name = "Milan"
print(milan.name, milan.language, milan.salary)

# print(employee.language, employee.salary)

# Here name is an instance variable and language and salary are class variables. Instance variables are unique to each instance of a class. Class variables are shared by all instances of the class.

# The class variable is shared by all instances of the class. The instance variable is unique to each.


