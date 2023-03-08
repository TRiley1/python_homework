class Customer:
    def __init__(self, name, age, wallet):
       self.name = name 
       self.age = age
       self.wallet = wallet
       self.level = 0

    def buy_drink(self, drink):
        self.wallet -= drink.price 
    
    def drunkness_level(self, drink):
        self.level += drink.alcohol_level
    
