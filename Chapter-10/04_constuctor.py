class employee:
    language = "Python"
    salary = 120000

    def __init__(self, name, salary, language):  # constructor or dunder method"
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is ${self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")


raja = employee("Raja", 130000, "Java")
raja.name = "Raja"

raja.greet()
raja.getInfo()
