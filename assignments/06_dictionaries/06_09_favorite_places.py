"""
Blake Anaman-Williams
difficulty is a 4/10
"""


favorite_places = {
    'Blake': ['New York', 'Ghana', 'Miami'],
    'Sarah': ['Paris', 'London'],
    'Michael': ['Tokyo', 'Los Angeles', 'Dubai']
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"{place}")
   