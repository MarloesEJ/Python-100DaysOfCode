from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

running = True

myMenu = Menu()
myCoffeeMaker = CoffeeMaker()
myMoneyMachine = MoneyMachine()

while running:
    options = myMenu.get_items()
    whatCoffee = input(f"What would you like? ({options}): ").lower()
    if whatCoffee == "off":
        running = False
    elif whatCoffee == "report":
        myCoffeeMaker.report()
        myMoneyMachine.report()
    elif myMenu.find_drink(whatCoffee):
        drink = myMenu.find_drink(whatCoffee)
        if myCoffeeMaker.is_resource_sufficient(drink):
            print(f"your {whatCoffee} costs: ${drink.cost}")
            if myMoneyMachine.make_payment(drink.cost):
                myCoffeeMaker.make_coffee(drink)
