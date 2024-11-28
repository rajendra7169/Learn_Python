# Q-2 Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

mark1 = int(input("Enter your mark: "))
marks.append(mark1)

mark2 = int(input("Enter your mark: "))
marks.append(mark2)

mark3 = int(input("Enter your mark: "))
marks.append(mark3)

mark4 = int(input("Enter your mark: "))
marks.append(mark4)

mark5 = int(input("Enter your mark: "))
marks.append(mark5)

mark6 = int(input("Enter your mark: "))
marks.append(mark6)

marks.sort()
print(marks)
