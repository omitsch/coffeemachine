

def check_resources(input_resources, product_ingredients):
    for resource in input_resources:
        if resource > product_ingredients:
            return f""

# def calculalte_coins(input_quarters, input_dimes, input_nickles, input_pennies):
#     input_quarters * 0.25
#     input_dimes * 0.10
#     input_nickles * 0.05
#     input_pennies * 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# TODO: Coins: Penny = 1 cent, Nickel = 5 cents, Dime = 10 cents, Quarter = 25 cents

# TODO: Print report -> How much resources left?
drink = input("What would you like? espresso/latte/cappuccino? ")
if drink == "report":
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n")
else:
    # FIXME:
    print("Please insert coins")
    quarters = int(input(f"How many quarters?: ")) * 0.25
    dimes = int(input(f"How many dimes?: ")) * 0.10
    nickles = int(input(f"How many nickles?: ")) * 0.05
    pennies = int(input(f"How many pennies?: ")) * 0.01
    budget = quarters + dimes + nickles + pennies
    drink = MENU[drink]
    price = drink[cost]
    print(price)
    # print(budget - price)




# TODO: Check if resources sufficient
# TODO: Process coins. Enough money? -> calculate change -> handover drink & enjoy. else refund money

c = 1000
#okay