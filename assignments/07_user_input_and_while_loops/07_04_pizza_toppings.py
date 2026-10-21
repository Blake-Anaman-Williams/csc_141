"""
Blake Anaman-Williams
Difficulty is a 3/10
"""


pizzas = True
while pizzas:
    topping = input("What topping would you like on your pizza? ")
    if topping == 'quit':
        pizzas = False
    else:
        print(f"we will add{topping} to your pizza.")