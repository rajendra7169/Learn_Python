class employee:
    language = "Python"
    salary = 120000

    def getInfo(self):  # self is a reference to the current instance of the class
        print(f"The language is {self.language}. The salary is ${self.salary}")

    @staticmethod  # This is a static method which is called decorator
    def greet():
        print("Good Morning!")


raja = employee()
raja.name = "Raja"

raja.greet()
raja.getInfo()
# employee.getInfo(raja)
