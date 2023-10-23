from reference import MENU
from reference import resources


# This function takes a user prompt and returns the appropriate status code.
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


# This function takes the user status code and returns the appropriate type of coffee.
def coffee_type(choice):
    """Gets the coffee type the user chose"""
    if choice == 1:
        return "espresso"
    elif choice == 2:
        return "latte"
    else:
        return "cappuccino"


# This function displays a report of available resources and what profits have been made.
def report(money):
    """Displays a report of available resources and profits."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")    


# This function checks what resources are left and whether they are enough to make the user's coffee.
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
    

# This function asks for an amount of coins for each US coin type from the user.
def insert_coins():
    """Gets coins from the user."""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return total


# This function checks if the user paid enough for their coffee, and returns change if any.
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


# This function takes the resources needed to make the user's coffee, and returns the coffee's cost.
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


# This function is the main function that drives all the other functions.
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
    

# Run the coffee machine until it is turned off.
running = 1.0
money = 0
while running >= 0:
    running = coffee_machine(money)
    if running > 0:
        money += running