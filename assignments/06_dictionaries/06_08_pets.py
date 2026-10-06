"""
Blake Anaman-Williams
difficulty is a 4/10
"""


pet_1 = {
    'animal': 'dog',
    'owner': 'Blake'
}

pet_2 = {
    'animal': 'cat',
    'owner': 'Sarah'
}

pet_3 = {
    'animal': 'bird',
    'owner': 'Michael'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    