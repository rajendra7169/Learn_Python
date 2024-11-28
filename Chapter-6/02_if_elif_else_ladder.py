# If elif else ladder example:

licence_age = int(input("Enter your age: "))

if licence_age < 0:
    print("Invalid input. Please enter a valid age.")

elif licence_age == 0:
    print("You have entered 0. Please enter a valid age.")

elif licence_age < 18:
    print("You are not eligible for driving licence.")

elif 18 <= licence_age <= 65:
    print("You are eligible for driving licence.")

else:
    print("You are not eligible for driving licence.")

print("Thank you for using our service.")

# If elif and else run in a sequence. If the first condition is true, the code block under that condition will run and the rest of the code will be skipped. If the first condition is false, the next condition will be checked and so on. If none of the conditions are true, the else block will run.
