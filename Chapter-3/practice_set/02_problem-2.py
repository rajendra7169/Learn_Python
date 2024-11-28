# Write a program to fill in a letter template givien below with name and date:
""" Dear < |Name| >
    You are selected!
    < |Date| >
"""
from datetime import date  # Importing current date

name = input("Enter Your Name: ")
date = date.today()  # Function for use current date

print(f"Dear {name} \nYou are selected! \n{date}")

# OR using method chaining

letter = """Dear <|Name|>
You are selected!
<|Date|>"""

print(letter.replace("<|Name|>", "Raja").replace("<|Date|>", "2025-09-12"))
