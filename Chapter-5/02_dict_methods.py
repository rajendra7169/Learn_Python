marks = {
    "Raja": 100,
    "Rohan": 79,
    "Suman": 80,
    "Sujan": 35,
    "list": [12, 56, 78],
    0: "Roshan",
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update(
    {"Raja": 99, "Renuka": 100}
)  # We can add or update new key and value in remaining items
print(marks)


print(marks.get("Raja1"))  # Prints None if value does not exist
print(marks["Raja1"])  # Returns an error if value does not exist
