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
    """Displays a report of available resources and profits."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")    


def resource_check(choice):
    """Checks available resources."""
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
    

def insert_coins():
    """Gets coins from the user."""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return total


def check_money(choice, amount):
    """Checks if the amount the user paid is enough for their coffee."""
    if amount < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        money += MENU[choice]["cost"]
        if amount > MENU[choice]["cost"]:
            change = amount - MENU[choice]["cost"]
            print(f"Here is ${round(change, 2):.2f} in change.")
        return True


def make_coffee(choice):
    """Makes the user's coffee"""
    if choice == 1:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        print("Here is your espresso. Enjoy!")
    elif choice == 2:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        print("Here is your latte. Enjoy!")
    else:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        print("Here is your cappuccino. Enjoy!")


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
        if ingredients:
            print("Please insert coins.")
            purchase_amount = insert_coins()
            if check_money(prompt, purchase_amount):
                make_coffee(prompt)
                
    return 1
    

running = 1
while running == 1:
    running = coffee_machine()