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



def process_coins():
    quarters=int(input("how many quarters : "))
    dimes=int(input("how many dimes : "))
    nickles=int(input("how many nickles : "))
    pennis=int(input("how many pennis : "))
    money = 0.25*quarters + 0.1*dimes+0.05*nickles+0.01*pennis
    return round(money,2)



def print_report(money):
    print(f" water : {resources["water"]}")
    print(f" milk : {resources["milk"]}")      
    print(f" coffee :{resources["coffee"]}")
    print(f"money : ${money}")



def is_sufficient_(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


money = 0
is_on = True
while is_on:
    choice= input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    

    if choice== "report":
        print_report(money)
        continue
    elif choice == "off":
        break
    elif choice not in MENU.keys():
        print (f"{choice} is an  invalid enrty")
        continue

    Coffe_type= MENU[choice]
    Ingradiants=Coffe_type["ingredients"]
    Cost= Coffe_type["cost"]

    if is_sufficient_(Ingradiants):
        payment= process_coins()
        if payment > Cost:
            change = payment -Cost
            print (f"retuen the change{change} ")
        else:
            print ("SOORY , NOT ENOUGH MONEY")
        if change >0 :
            money+=Cost
        for item in Ingradiants:
            resources[item]-=Ingradiants[item]

        print(f"Here is your {choice} ☕️. Enjoy!")
        





