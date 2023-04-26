from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


beverage= None
drinks=Menu()
order=CoffeeMaker()
transactions=MoneyMachine()

while beverage !="off":

    available_drinks=drinks.get_items()

    beverage= input(f"​What would you like? {available_drinks} :​")

    if beverage== "off":
        print("See you later!")
    elif beverage=="report":

        order.report()
        transactions.report()
    else:
        chosen_available_drink=drinks.find_drink(beverage)

        if chosen_available_drink != None:
            can_make=order.is_resource_sufficient(chosen_available_drink)
            if can_make==True:
                is_payment_accepted= transactions.make_payment(chosen_available_drink.cost)

                if is_payment_accepted==True:
                    order.make_coffee(chosen_available_drink)
                    


    

    








