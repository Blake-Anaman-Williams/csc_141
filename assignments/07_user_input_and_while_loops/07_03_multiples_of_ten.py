"""
Blake Anaman-Williams
Difficulty is a 3/10
"""

chosen_number = input("Please enter a number: ")
yes_or_no = int(chosen_number) % 10
if yes_or_no == 0:
   print(f"{chosen_number} is a multiple of 10!")
else:
    print(f"{chosen_number} is not a multiple of 10.")
