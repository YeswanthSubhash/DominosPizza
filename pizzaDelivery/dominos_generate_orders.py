import random
from datetime import datetime
from pizzaDelivery.dominos_collect_details import collect_details


class generate_details(collect_details):

    def __init__(self):
        super().__init__()

    def generate_orders(self):
        # Each Order can have 1-10 pizzas in it
        pizza_price = 0
        toppings_price = 0
        beverage_price = 0
        pizzas = []
        for pizza in range(random.randint(1, self.MAX_NO_OF_PIZZA)):
            toppings = []
            for topping in range(random.randint(1, self.MAX_NO_OF_TOPPINGS)):
                toppings.append(self.toppings_menu())
                toppings_price = toppings_price + random.randint(35, 85)
            beverages = []
            for beverage in range(random.randint(0, self.MAX_NO_OF_BEVERAGES)):
                beverages.append(self.beverages_menu())
                beverage_price = beverage_price + random.randint(35, 85)
            pizzas.append({"pizzaName": self.pizza_menu(), "toppings": toppings, "beverages": beverages})
            pizza_price = pizza_price + random.randint(200, 750)
        cgst = 5
        sgst = 5
        total_tax_perc = cgst + sgst
        totalAmount = pizza_price + toppings_price + beverage_price
        totalAmount_incl_tax = ((totalAmount * total_tax_perc) / 100) + totalAmount

        order_and_price = {'totalorders':pizzas,
                           'totalamountpizza':totalAmount,
                           'totalamountincltax':totalAmount_incl_tax
        }
        return order_and_price

    def generate_message(self,orderId,fake):

        stores = self.stores_locations(fake)
        delivery = self.delivery_locations(fake)
        orders = self.generate_orders()
        customer = self.customer_details(fake)

        message = {
            "storeaddress": stores['storeAddress'],
            "storelatitude": stores['storeLatitude'],
            'storelongitude': stores['storeLongitude'],
            'storephonenumber': stores['storePhoneNumber'],
            'customername': customer['customername'],
            'customeraddress': customer['customeraddress'],
            'customerphonenumber': customer['customerphonenumber'],
            'customeremail': customer['customeremail'],
            'delivaryaddress': delivery['delivaryAddress'],
            'delivarylatitude': delivery['delivaryLatitude'],
            'delivarylongitude': delivery['delivaryLongitude'],
            'delivaryphoneNumber': delivery['delivaryPhoneNumber'],
            'orderid':orderId,
            'orders': orders['totalorders'],
            'totalamountpizza': orders['totalamountpizza'],
            'totalamountincltax': orders['totalamountincltax'],
            'date':datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),


        }

        return message





