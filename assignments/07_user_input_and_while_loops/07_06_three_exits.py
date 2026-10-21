"""
Blake Anaman-Williams
Difficulty is a 6/10
needed help from google
"""
topping = ""

while topping != 'quit':
    topping = input("What topping would you like on your pizza? ")

    if topping != 'quit':
        print(f"We will add {topping} to your pizza.")





pizzas = True

while pizzas:
    topping = input("What topping would you like on your pizza? ")

    if topping == 'quit':
        pizzas = False
    else:
        print(f"We will add {topping} to your pizza.")





while True:
    topping = input("What topping would you like on your pizza? ")

    if topping == 'quit':
        break
    else:
        print(f"We will add {topping} to your pizza.")
