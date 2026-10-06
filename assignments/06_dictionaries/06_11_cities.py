"""
Blake Anaman-Williams
difficulty is a 5/10
"""


cities = {
    'New York': {
        'country': 'United States',
        'population': '100 million',
        'fact': 'It is home to Times Square.'
    },
    'Accra': {
        'country': 'Ghana',
        'population': '500 million',
        'fact': 'It is the capital city of Ghana.'
    },
    'Barcelona': {
        'country': 'Spain',
        'population': '300 million',
        'fact': 'It has a good football team.'
    }
}

for city, information in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")