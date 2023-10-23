from reference import MENU
from reference import resources

# TODO: 1. Prompt user for coffee
# TODO: 2. Turn off coffee machine from 'off' prompt
# TODO: 3. Print report
# TODO: 4. Check that resources are sufficient
# TODO: 5. Process coins
# TODO: 6. Check transaction successful
# TODO: 7. Make coffee
money = 0


def command(choice):
    """Executes a user command"""
    if choice == "off":
        return -1
    elif choice == "report":
        return 0
    elif choice == "espresso":
        return 1
    elif choice == "latte":
        return 2
    elif choice == "cappuccino":
        return 3
    else:
        print("Next time, please enter the name correctly")
        return -1


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")    


def resource_check(choice):
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    
    if choice != 1 and MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    
    if MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    
    return True
    

def coffee_machine():
    """Coffee Machine"""
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    status = command(prompt)
    if status == -1:
        return 0
    elif status == 0:
        report()
    else:
        ingredients = resource_check(prompt)
    return 1
    

running = 1
while running == 1:
    running = coffee_machine()