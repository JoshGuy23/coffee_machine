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


def command(prompt):
    """Executes a user command"""
    if prompt == "off":
        return -1
    elif prompt == "report":
        return 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")    


def coffee_machine():
    """Coffee Machine"""
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    status = command(prompt)
    if status == -1:
        return 0
    elif status == 0:
        report()
    return 1
    

running = 1
while running == 1:
    running = coffee_machine()