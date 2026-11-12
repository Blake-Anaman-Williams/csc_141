def make_sandwich(*items):
    print("Your sandwich contains:")

    for item in items:
        print(item)

make_sandwich("Chicken")
make_sandwich("Ham", "Cheese")
make_sandwich("Turkey", "Lettuce", "Tomato")