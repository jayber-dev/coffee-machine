from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


exit = "on"

while exit == "on":
    options = menu.get_items()
    user_choice = input(f"what would you like to have ? {options}")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        exit = "off"
    else:
        user_drink = menu.find_drink(user_choice)
        is_ing_ok = coffee_maker.is_resource_sufficient(user_drink)
        is_money_ok = money_machine.make_payment(user_drink.cost)
        
        if is_ing_ok and is_money_ok:
            coffee_maker.make_coffee(user_drink)
        
