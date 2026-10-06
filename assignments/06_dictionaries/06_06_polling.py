"""
Blake Anaman-Williams
difficulty is a 4/10
"""


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people_to_poll = ['blake', 'sarah', 'phil', 'david']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person}, for responding to the poll.")
    else:
        print(f"{person}, please take our favorite languages poll.")