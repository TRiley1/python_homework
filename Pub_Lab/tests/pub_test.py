import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Crass Badger", 100.00)
        self.drink = Drink("Beer", 3.00, 3)
        self.customer = Customer("Jammo", 24, 10.00)
        self.customer2 = Customer("Timmy",12, 5.00)

    def test_pub_name(self):
        self.assertEqual("The Crass Badger", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(100.00, self.pub.till)

    # def test_got_drink(self, drink):
    #     self.assertEqual(True, )

    def test_sell_drink_pass(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(103.00, self.pub.till)
        self.assertEqual(7, self.customer.wallet)

    def test_sell_drink_fail(self):
        decline = self.pub.sell_drink(self.drink, self.customer2)
        self.assertEqual("NO!!", decline)
