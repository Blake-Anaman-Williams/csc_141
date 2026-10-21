"""
Blake Anaman-Williams
Difficulty is a 1/10
"""


number_of_people = input("How many people are in your party? ")

if int(number_of_people) > 8:
    print("You'll have to wait for a larger table.")
else:
    print("Your table is ready!")