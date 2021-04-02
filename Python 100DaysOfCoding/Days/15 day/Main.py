
# menu
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

# TODO: 1.Write amount of an ingredients

profit = 0

# TODO: 2.Coins
def insert_coins():
    total = 0
    print("Please insert coins.")
    inp_quarters = int(input("How many quarters?: "))
    quarters = inp_quarters * 0.25

    inp_dimes = int(input("How many dimes?: "))
    dimes = inp_dimes * 0.1

    inp_nickel = int(input("How many nickels?: "))
    nickels = inp_nickel * 0.05

    inp_penny = int(input("How many pennies?: "))
    penny = inp_penny * 0.01

    total += quarters + dimes + nickels + penny
    return total

# TODO: 3.Check, are resources sufficient?
def is_resources_sufficient(order):
    for i in order:
        if order[i] > resources[i]:
            print(f"Sorry, there is not enough {i}")
            return False

    return True

# TODO: 4. Check is transaction was successful?
def is_transaction_successful(inserted_coins, coffee_cost):
    if inserted_coins >= coffee_cost:
        change = round(inserted_coins - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def make_coffee(coffee_name, order_ingredients):
    for i in order_ingredients:
        resources[i] = resources[i] - order_ingredients[i]
    print(f"Here is your {coffee_name} ☕. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml" +
              f"\nMilk: {resources['milk']}ml" +
              f"\nCoffee: {resources['coffee']}gr" +
              f"\nMoney: ${profit}")
    else:
        if is_resources_sufficient(MENU[choice]["ingredients"]):
            inserted_coins = insert_coins()
            check_sum = is_transaction_successful(inserted_coins, MENU[choice]["cost"])
            if check_sum == True:
                make_coffee(choice, MENU[choice]["ingredients"])

