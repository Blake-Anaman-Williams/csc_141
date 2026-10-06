"""
Blake Anaman-Williams
difficulty is a 4/10
"""


rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers:")
for river in rivers:
    print(river)

print("\nCountries:")
for country in rivers.values():
    print(country)