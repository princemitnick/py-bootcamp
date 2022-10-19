from coffee_resources import resources
from coffee_flavours import MENU


def report():
    global resources
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Money : {profit}")


def process_coins(quarters, dimes, nickles, pennies):
    return round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)


def set_resources(current_resources, flavours, money):
    current_resources['water'] = current_resources['water'] - flavours['ingredients']['water']
    current_resources['coffee'] = current_resources['coffee'] - flavours['ingredients']['coffee']
    current_resources['milk'] = current_resources['milk'] - flavours['ingredients']['milk']



profit = 0
def make_coffee(flavours_taken):

    global resources
    global  profit
    if flavours_taken == 'espresso':
        flavours = MENU['espresso']
    if flavours_taken == 'latte':
        flavours = MENU['latte']
    if flavours_taken == 'cappuccino':
        flavours = MENU['cappuccino']

    if resources['coffee'] < flavours['ingredients']['coffee']:
        print("Sorry, there is not enough coffee.")
    elif resources['water'] < flavours['ingredients']['water']:
        print("Sorry, there is not enough water.")
    elif resources['milk'] < flavours['ingredients']['milk']:
        print("Sorry, there is not enough mater.")
    else:
        print("Please insert coin")
        quarters = float(input("How many quarters? : "))
        dimes = float(input("How many dimes? : "))
        nickles = float(input("How many dimes? : "))
        pennies = float(input("How many dimes? : "))
        profit = process_coins(quarters, dimes, nickles, pennies)
        if profit < flavours['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if profit > flavours['cost']:
               change = round((profit - flavours['cost']), 2)
               print(f'Here your {change} in change.')
               print("Here your late. Enjoy!")
            else:
                print(f"Here your {flavours_taken}. Enjoy!")

            profit = flavours
            set_resources(resources, flavours, flavours['cost'])
            report()


decision = None

while decision != 'off':
    decision = input("What would you like? (espresso/latte/cappuccino): ")
    if decision == "report":
        report()
    elif decision == 'espresso':
        make_coffee(decision)
    elif decision == 'latte':
        make_coffee(decision)
    elif decision == 'cappuccino':
        make_coffee(decision)
    elif decision == 'off':
        decision == 'off'
