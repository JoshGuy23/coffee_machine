from reference import MENU
from reference import resources

# TODO: 1. Prompt user for coffee
# TODO: 2. Turn off coffee machine from 'off' prompt
# TODO: 3. Print report
# TODO: 4. Check that resources are sufficient
# TODO: 5. Process coins
# TODO: 6. Check transaction successful
# TODO: 7. Make coffee


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


def coffee_type(choice):
    if choice == 1:
        return "espresso"
    elif choice == 2:
        return "latte"
    else:
        return "cappuccino"


def report(money):
    """Displays a report of available resources and profits."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")    


def resource_check(choice):
    """Checks available resources."""
    coffee = coffee_type(choice)
    if MENU[coffee]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    
    if choice != 1:
        if MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
    
    if MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
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
    coffee = coffee_type(choice)
    if amount < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if amount > MENU[coffee]["cost"]:
            change = amount - MENU[coffee]["cost"]
            print(f"Here is ${round(change, 2):.2f} in change.")
        return True


def make_coffee(choice):
    """Makes the user's coffee"""
    coffee = coffee_type(choice)
    if choice == 1:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        print("Here is your espresso. Enjoy!")
    elif choice == 2:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        print("Here is your latte. Enjoy!")
    else:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        print("Here is your cappuccino. Enjoy!")
    return MENU[coffee]["cost"]


def coffee_machine(money):
    """Coffee Machine"""
    profit = money
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    status = command(prompt)
    if status == -1:
        return -1
    elif status == 0:
        report(profit)
        return 0
    else:
        profit = 0
        ingredients = resource_check(status)
        if ingredients:
            print("Please insert coins.")
            purchase_amount = insert_coins()
            if check_money(status, purchase_amount):
                profit += make_coffee(status)            
        return profit
    

running = 1.0
money = 0
while running >= 0:
    running = coffee_machine(money)
    if running > 0:
        money += running