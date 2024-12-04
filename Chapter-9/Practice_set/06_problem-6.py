# Q-6 Write a program to mine a log file and find out whether it contains ‘python’.

word = "python"

with open("Chapter-9/Practice_set/Log.txt", "r") as f:
    conetnt = f.read()

if word in conetnt:
    print("This log file content content 'Python' word")
else:
    print("This log file does not content content 'Python' word")
