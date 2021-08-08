import random

class collect_details:

    def __init__(self):
        self.MAX_NO_OF_PIZZA = 8
        self.MAX_NO_OF_TOPPINGS = 10
        self.MAX_NO_OF_BEVERAGES = 3

    def stores_locations(self, fake):
        storeAddress = fake.address()
        storeLatitude = str(fake.latitude())
        storeLongitude = str(fake.longitude())
        storePhoneNumber = fake.phone_number()

        store_loc = {'storeAddress': storeAddress,
                     'storeLatitude': storeLatitude,
                     'storeLongitude': storeLongitude,
                     'storePhoneNumber': storePhoneNumber
                     }

        return store_loc

    def delivery_locations(self,fake):
        delivaryAddress = fake.address()
        delivaryLatitude = str(fake.latitude())
        delivaryLongitude = str(fake.longitude())
        delivaryPhoneNumber = fake.phone_number()

        delivary_loc = {'delivaryAddress': delivaryAddress,
                     'delivaryLatitude': delivaryLatitude,
                     'delivaryLongitude': delivaryLongitude,
                     'delivaryPhoneNumber': delivaryPhoneNumber
                     }

        return delivary_loc

    def pizza_menu(self):
        validPizzaNames = ['Margherita',
                           'Marinara',
                           'Diavola',
                           'Mari & Monti',
                           'Salami',
                           'Pepperoni'
                           ]
        return validPizzaNames[random.randint(0, len(validPizzaNames) - 1)]

    def toppings_menu(self):
        validPizzaNames = ['Broccoli',
                           'Pancetta',
                           'Gorgonzola',
                           'Mushroom',
                           'Black olives',
                           'Anchovies',
                           'Radicchio',
                           'Capers',
                           'Eggplant',
                           'Capsicum',
                           'Speck',
                           'Bacon'
                           ]
        return validPizzaNames[random.randint(0, len(validPizzaNames) - 1)]

    def beverages_menu(self):
        validPizzaNames = ['Pepsi',
                           'Mirinda',
                           'Coca Cola',
                           '7 up',
                           'Thums Up',
                           'Fanta'
                           ]
        return validPizzaNames[random.randint(0, len(validPizzaNames) - 1)]










