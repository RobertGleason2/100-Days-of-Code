# Project simulates a coffee machine making coffee by creating coffee machine, money machine, menu and menu item ojects.
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    machine_on = True
    # creates new objects to be callled and used
    coffee_machine = CoffeeMaker()
    money_mahine = MoneyMachine()
    menu = Menu()
    while machine_on:
        user_input = input("What would you like? (expresso/latte/cappuccino) ").lower()
        if user_input == "off":
            machine_on = False
        elif user_input == "report":
            coffee_machine.report()
            money_mahine.report()
        else:
            # searches for drink name and returns menu item object if found
            drink = menu.find_drink(user_input)
            if coffee_machine.is_resource_sufficient(drink):
                # checks if money payement if sufficent
                if money_mahine.make_payment(drink.cost):
                    # creates drink and subrtacts resources from 
                    coffee_machine.make_coffee(drink)
main()


