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

# TODO: Maschieneninhalt -> 300ml Wasser, 200ml Milch, 100g Kaffee
#   Coins: Penny = 1 cent, Nickel = 5 cents, Dime = 10 cents, Quarter = 25 cents

# TODO: Print report -> How much resources left?
wish = input("What would you like? espresso/latte/cappuccino? ")
if wish == "report":
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n")


# TODO: Check if resources sufficient
# TODO: Process coins. Enough money? -> calculate change -> handover drink & enjoy. else refund money

# Einfach nur ein test ob das funktioniert
b = 100
