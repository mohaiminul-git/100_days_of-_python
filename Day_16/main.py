

from coffee_maker import CoffeeMaker
from menu import MenuItem,Menu
from money_machine import MoneyMachine

menu=Menu()
coffe_maker=CoffeeMaker()
payment=MoneyMachine()

is_on = True
while is_on:
    choice= input(f"What would you like?{menu.get_items()}")

    if choice == "report":
        coffe_maker.report()
        payment.report()
        continue
    elif choice == "off":
        is_on=False

    else:
        drink=menu.find_drink(choice)

        if coffe_maker.is_resource_sufficient(drink) and payment.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)




    




