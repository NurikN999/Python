from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()

cm = CoffeeMaker()


is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f'What would you like?{option}:')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        cm.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                cm.make_coffee(drink)