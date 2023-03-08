import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Crass Badger", 100.00)
        self.drink = Drink("Beer", 3.00, 3)
        self.drink2 = Drink("Paint Stripper", 2.00, 20)
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

    def test_sell_drink_fail_too_young(self):
        decline = self.pub.sell_drink(self.drink, self.customer2)
        self.assertEqual("NO!!", decline)

    def test_to_drunk_too_order(self):
        self.customer.drunkness_level(self.drink2)
        decline = self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual("NO!!", decline)
