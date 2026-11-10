class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range

    def describe_restaurant(self):
        print(f'The restuarant name is {self.restaurant_name}')
        print(f'The price is {self.price_range}')

    def can_you_take_a_date(self):
        if self.price_range < 50:
            print(f"Dont embarass yourself. It's expensive!")
        else:
            print(f"You can afford {self.restaurant_name}.")

ev_restaurant = Restaurant('Cici shack', 'Fast food', 'Accra', 30)
ev_restaurant.can_you_take_a_date()
