class Pub:
    def __init__(self, name, till):
        self.name = name 
        self.till = till
        self.drinks = []

    def got_drink(self, drink):
        if drink: 
            return True
    
    
    def sell_drink(self, drink, customer):
        if customer.age >= 18 and customer.level < 10: 
            self.till += drink.price
            customer.buy_drink(drink)
        return "NO!!"


    # and alcohol_level < 10: