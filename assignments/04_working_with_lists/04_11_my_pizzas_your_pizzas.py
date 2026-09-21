""" 
Blake Anaman-Williams

This progrqam is suposed to list my favorite pizzas 
and my friends favorite pizzas and amending the list of pizzas and printing them out
"""



pizzas = ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken"]

friend_pizzas = pizzas[:]  

pizzas.append('Tuna Pizza')
friend_pizzas.append('Cheese Pizza')

print("My favorite pizzas are:")
for pizzas in pizzas:
    print(pizzas)

print("My friend's favorite pizzas are:")
for friend_pizzas in friend_pizzas:
    print(friend_pizzas)
