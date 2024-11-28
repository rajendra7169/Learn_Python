# Q-2 Write a program to find out whwther a student has passed or faild if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter the marks of subject 1: "))
sub2 = int(input("Enter the marks of subject 2: "))
sub3 = int(input("Enter the marks of subject 3: "))

total = sub1 + sub2 + sub3
percentage = total / 3

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and percentage >= 40:
    print("You have passed the exam.")
    print(f"You have got {percentage:.2f}%")
    print(f"You have got {(sub1*100)/100}% in first subject.")
    print(f"You have got {(sub2*100)/100}% in second subject.")
    print(f"You have got {(sub3*100)/100}% in third subject.")

else:
    print("You have failed the exam.")
    print(f"You have got {percentage:.2f}%")
    print(f"You have got {(sub1*100)/100}% in first subject.")
    print(f"You have got {(sub2*100)/100}% in second subject.")
    print(f"You have got {(sub3*100)/100}% in third subject.")
