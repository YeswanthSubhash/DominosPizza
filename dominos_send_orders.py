from faker import Faker
from pizzaDelivery.dominos_generate_orders import generate_details
import random



if __name__ == "__main__":

    fake = Faker('en_IN')
    self = generate_details()
    print(self)

    for i in range(1,10):
        message = self.generate_message(str(random.randint(50,1000)),fake)
        print(message)