from reference import MENU
from reference import resources

# TODO: 1. Prompt user for coffee
# TODO: 2. Turn off coffee machine from 'off' prompt
# TODO: 3. Print report
# TODO: 4. Check that resources are sufficient
# TODO: 5. Process coins
# TODO: 6. Check transaction successful
# TODO: 7. Make coffee


def command(prompt):
    """Executes a user command"""
    if prompt == "off":
        return -1


def coffee_machine():
    """Coffee Machine"""
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    status = command(prompt)
    if status == -1:
        return 0
    

running = 1
while running == 1:
    running = coffee_machine()