"""
Blake Anaman-Williams
difficulty is a 4/10
"""


person_1 = {
    'first_name': 'Blake',
    'last_name': 'Anaman-Williams',
    'age': 30,
    'city': 'Los Angeles'
}

person_2 = {
    'first_name': 'Michael',
    'last_name': 'Smith',
    'age': 19,
    'city': 'New York'
}

person_3 = {
    'first_name': 'Sarah',
    'last_name': 'Johnson',
    'age': 18,
    'city': 'Philadelphia'
}

people = [person_1, person_2, person_3]

for person in people:
    print(person)