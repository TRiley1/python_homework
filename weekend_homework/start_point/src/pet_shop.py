# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, money):
    pet_shop["admin"]["total_cash"] += money

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sales):
    pet_shop["admin"]["pets_sold"] += sales

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# def get_pets_by_breed(pet_shop, breed):
#     pets = []

#     for pet in pet_shop["pets"]:
#         if  pet["breed"] == breed:
#             pets.append(pet["name"])

#     return pets

def get_pets_by_breed(pet_shop, breed):
    pets = []

    for pet in pet_shop["pets"]:
        if breed in pet["breed"]:
            pets.append(pet["name"])

    return pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if name in pet["name"]:
            return pet
    return None

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if name in pet["name"]:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
     return customers["cash"]
    

def remove_customer_cash(customers, cash):
     customers["cash"] -= cash  
  
def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    money = get_customer_cash(customer)
    if money >= new_pet["price"]:
        return True
    return False
    
# on to 'integration' tests. Multiple conditions! 

def sell_pet_to_customer(pet_shop, pet, customer):
    
    if pet not in pet_shop["pets"] or customer["cash"] < pet["price"]:
        return None
    
    pet_price = pet["price"]
    # access customer pets .. append pet there 
    customer["pets"].append(pet)
    # access pets_sold add 1
    pet_shop["admin"]["pets_sold"] += 1
    # remove pet price from customer money 
    customer["cash"] -= pet_price
    # increase total shop money by pet price
    pet_shop["admin"]["total_cash"] += pet_price

