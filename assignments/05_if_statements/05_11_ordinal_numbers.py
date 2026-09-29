"""Blake Anaman-Wiiliams
This is my work 
This program prints out the ordinal numbers for the numbers 1 to 9.
"""



numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")