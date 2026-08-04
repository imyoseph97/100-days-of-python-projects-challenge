
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



def money_in_coin():
    quarter = float(input("How many quarters? "))
    quarter *= 0.25
    dime = float(input("How many dimes? "))
    dime *= 0.10
    nickel = float(input("How many nickeles? "))
    nickel *= 0.05
    penny = float(input("How many pennies? "))
    penny *= 0.01

    total = quarter + dime + nickel + penny
    
    return round(total, 2) 

def sold():
    for e in drink["ingredients"]:
        resources[e] -= drink["ingredients"][e]


money = 0


enough = True

is_machine_on = True

while is_machine_on:
    
    barista = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if barista in MENU:
        drink = MENU[barista]
        for e in drink["ingredients"]:
            if resources[e] < drink['ingredients'][e]:
                print(f"Sorry, there's no enough {e}.")
                enough = False
        if enough == True:
            T = money_in_coin()
            change = T - drink['cost']
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here's ${change} in change")
                print(f"Here's your {e}, Enjoy! ☕")
                sold()
                money += drink['cost']
    elif barista == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${money}")
    elif barista == 'off':
        break
    
