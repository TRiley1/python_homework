import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jammo",23, 10.00)
        self.drink = Drink("beer", 3.00, 3, 5)
        self.drink2 = Drink("wine", 5.00, 5, 5)
        self.pub = Pub("The Crass Badger", 100.00)

    def test_customer_name(self):
        self.assertEqual("Jammo", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(7.00, self.customer.wallet)

    def does_level_increase(self):
        drink1 = self.customer.drunkness_level(self.drink)
        drink2 = self.customer.drunkness_level(self.drink2)
        self.assertEqual(8, self.customer.level )