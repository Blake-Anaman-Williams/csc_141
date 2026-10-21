"""
Blake Anaman-Williams
Difficulty is a 6/10
"""


sandwich_orders = [
    "tuna",
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami",
    "egg salad"
]

finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")

for sandwich in finished_sandwiches:
    print(sandwich)