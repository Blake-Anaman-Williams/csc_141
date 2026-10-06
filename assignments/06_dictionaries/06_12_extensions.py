"""
Blake Anaman-Williams
difficulty is a 6/10
"""


cities = {
    'New York': {
        'country': 'United States',
        'population': '100 million',
        'fact': 'It is home to Times Square.',
        'language': 'English'
    },
    'Accra': {
        'country': 'Ghana',
        'population': '500 million',
        'fact': 'It is the capital city of Ghana.',
        'language': 'English'
    },
    'Barcelona': {
        'country': 'Spain',
        'population': '300 million',
        'fact': 'It has a good football team.',
        'language': 'Catalan'
    }
}

for city, information in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
    print(f"Main language: {information['language']}")