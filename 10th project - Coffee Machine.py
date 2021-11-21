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
}
money = 0


def check_resources(desired_drink):
    for ingredient in MENU[desired_drink]["ingredients"]:
        if MENU[desired_drink]["ingredients"][ingredient] > resources[ingredient]:
            return ingredient
    else:
        return 1


def calculate_value(q, d, n, p):
    v = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    return v


def deduct_resources():
    for ingredient in MENU[customer_input]["ingredients"]:
        resources[ingredient] -= MENU[customer_input]["ingredients"][ingredient]


continue_working = True

while continue_working:
    customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_input == "report":
        print(f"Water: {resources['water']}" + "ml")
        print(f"Milk: {resources['milk']}" + "ml")
        print(f"Coffee: {resources['coffee']}" + "g")
        print(f"Money: ${money}")

    elif customer_input in MENU:
        check = check_resources(customer_input)
        if check == 1:
            print("Please insert coins. ")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            value = calculate_value(quarters, dimes, nickles, pennies)
            if value >= MENU[customer_input]["cost"]:
                money += MENU[customer_input]["cost"]
                change = round(value - MENU[customer_input]["cost"], 2)
                print(f"Here is ${change} in change.")
                deduct_resources()
                print(f"Here is your {customer_input}. Enjoy!☕")

            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {check}.")

    elif customer_input == "off":
        continue_working = False

    else:
        print("Please choose one of the following: espresso/latte/cappuccino. \n")
