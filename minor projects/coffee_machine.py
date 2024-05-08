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

def is_resource_sufficient(order_ingredients):
    """Returns true if resources are sufficient, Returns false if resources are not sufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return is_enough

def process_coins():
    """Returns the total coins inserted by the customer"""
    print("Please insert your coins")
    total = 0
    quarter = int(input("How many Quarters: ")) * 0.25
    dime = int(input("How many Dimes: ")) * 0.1
    nickel = int(input("How many Nickel: ")) * 0.05
    pennies = int(input("How many Pennies: ")) * 0.01

    total = quarter + dime + nickel + pennies
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accept, or return False when the money received is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(money_received=payment, drink_cost=drink["cost"]):
                make_coffee(drink_name= choice, order_ingredients= drink["ingredients"])

    
    


