# Q-1 Create a class “Programmer” for storing information of few programmers working at Microsoft.


class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address


employee_info = programmer("Raja", 12000, "Gothatar")
employee2_info = programmer("Milan", 13000, "Mulpani")
print(employee_info.name, employee_info.salary, employee_info.address)
print(employee2_info.name, employee2_info.salary, employee2_info.address)
