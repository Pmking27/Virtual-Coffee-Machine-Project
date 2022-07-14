from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_no = True

print(logo)
while is_no:
    options = menu.get_items()
    user_choice = input(f"What would you like ? ({options}):").lower()
    if user_choice == "off":
        print("coffee machine is off.")
        is_no = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice in options:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Invalid Choice")
        is_no = False
