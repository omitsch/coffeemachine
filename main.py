

def order():
    drink_wish = input("What would you like? espresso/latte/cappuccino? ")
    while drink_wish == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${resources['money']}\n")
        drink_wish = input("What would you like? espresso/latte/cappuccino? ")
    if drink_wish == "off":
        return False
    else:
        return drink_wish


def check_resources(drink_ingredients, input_resources):
    missing_ingredient = ""
    for ingredient in drink_ingredients:
        if drink_ingredients[f"{ingredient}"] > input_resources[f"{ingredient}"]:
            missing_ingredient = ingredient
    return missing_ingredient


def check_order(input_order):
    if input_order == "espresso" or "latte" or "cappuccino":
        missing_ingredient = check_resources(DRINK_INFO["ingredients"], resources)
        if missing_ingredient != "":
            print(f"Not enough {missing_ingredient}.")
        else:
            check_budget(resources)


def insert_coins():
    print("Please insert coins")
    quarters = int(input(f"How many quarters?: ")) * 0.25
    dimes = int(input(f"How many dimes?: ")) * 0.10
    nickles = int(input(f"How many nickles?: ")) * 0.05
    pennies = int(input(f"How many pennies?: ")) * 0.01
    budget = float(quarters + dimes + nickles + pennies)
    return budget


def check_budget(input_resources):
    budget = insert_coins()
    if budget < DRINK_INFO["cost"]:
        print("Sorry, not enough money. Money returned.")
    else:
        input_resources["money"] += DRINK_INFO["cost"]
        change = round(budget - DRINK_INFO["cost"], 2)
        if change == 0:
            print("Right on point, you don't need change!")
        else:
            print(f"Here is ${change} in change.")
        consume_resources(DRINK_INFO["ingredients"], resources)


def consume_resources(drink_ingredients, input_resources):
    for ingredient in drink_ingredients:
        input_resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {DRINK_WISH} ☕. Enjoy!")


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

new_order = True
while new_order:
    DRINK_WISH = order()
    if not DRINK_WISH:
        new_order = False
    else:
        DRINK_INFO = MENU[DRINK_WISH]
        check_order(DRINK_WISH)
