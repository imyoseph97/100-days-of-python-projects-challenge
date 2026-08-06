from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()


while True:
    barista = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if barista == "report":
        maker.report()
        money.report()
    elif barista in menu.get_items():
        drink = menu.find_drink(barista)
        if maker.is_resource_sufficient(drink):
            money.make_payment(drink.cost)
            maker.make_coffee(drink)
    elif barista == "off":
        break



