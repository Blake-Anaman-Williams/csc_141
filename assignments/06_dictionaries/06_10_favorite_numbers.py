"""
Blake Anaman-Williams
difficulty is a 5/10
"""


favorite_numbers = {
    'Blake': [67, 69, 21],
    'Michael': [1, 12],
    'Sarah': [2, 8, 156],
    'David': [115, 22],
    'Jessica': [4, 9]
}

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(number)
    