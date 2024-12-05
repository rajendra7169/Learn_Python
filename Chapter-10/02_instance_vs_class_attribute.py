class employee:
    language = "Python"
    salary = 120000


raja = employee()
raja.language = "JavaScript"  # This will change the language of raja to JavaScript beacuse instant attributes take precedence over class attributes
print(raja.salary, raja.language)

milan = employee()
milan.name = "Milan"
print(milan.name, milan.language, milan.salary)
