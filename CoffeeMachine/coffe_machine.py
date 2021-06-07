from Main import *
from art import logo
end_machine = False
insert_money = 0


# TODO: 3. Print report.
def print_report():
    count = 0
    for key, value in resources.items():
        if count == 0:
            print(key, ":", value, "ml")
            count = count + 1
        elif count == 1:
            print(key, ":", value, "ml")
            count = count + 1
        elif count == 2:
            print(key, ":", value, "g")
            count = count + 1
        elif count == 3:
            print(key, ":", "$", value)
    return


def choice_drink():
    user_choices = input("What would you like? (espresso/latte/cappuccino):")
    if user_choices == "espresso":
        return user_choices
    elif user_choices == "latte":
        return user_choices
    elif user_choices == "cappuccino":
        return user_choices
    elif user_choices == "off":
        off_machine = True
        print("Coffee machine is off")
        return off_machine
    elif user_choices == "report":
        print_report()
    else:
        print("Wrong choice, choose again please")
    return


# TODO: 4. Check resources sufficient?
#  a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
#  b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make
#  the drink but print: “Sorry there is not enough water.”
#  c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resources():
    #print(resources)
    check_ingredients = beverage["ingredients"]
    #print(check_ingredients)
    check = True
    for kind in check_ingredients:
        #print(kind)
        beverage_resource_need = check_ingredients[kind]
        #print(beverage_resource_need)
        if kind == "water":
            if resources["water"] < beverage_resource_need:
                print("Sorry there is not enough water.")
                check = False
                return check
        elif kind == "milk":
            if resources["milk"] < beverage_resource_need:
                print("Sorry there is not enough milk.")
                check = False
                return check
        elif kind == "coffee":
            if resources["coffee"] < beverage_resource_need:
                print("Sorry there is not enough coffee.")
                check = False
                return check
    return check


# TODO: 7a. Make Coffee.
def make_drink():
    #print(resources)
    ingredients = beverage["ingredients"]
    for supply in ingredients:
        #print(supply)
        machine_resources = ingredients[supply]
        #print(machine_resources)
        if supply == "water":
            resources["water"] = resources["water"] - machine_resources
        elif supply == "milk":
            resources["milk"] = resources["milk"] - machine_resources
        elif supply == "coffee":
            resources["coffee"] = resources["coffee"] - machine_resources
    #print(resources)
    return print(f"Here is your {user_pick}. ☕ Enjoy!")
# TODO: 7b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
#  If latte was their choice of drink


# TODO: 6. Check transaction successful?
def check_transaction(put_money):
    #print(beverage)
    beverage_cost = beverage["cost"]
    #print(beverage_cost)
    if beverage_cost <= put_money:
        change = round(put_money - beverage_cost, 2)
        print(f"Here is ${change} dollars in change.")
        resources["money"] = beverage_cost
        #print(resources["money"])
        transaction = True
        return transaction
    else:
        print("Sorry that's not enough money. Money refunded.")
        transaction = False
        return transaction

print(logo)
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt. a. For maintainers of the coffee machine, they
#  can use “off” as the secret word to turn off
while not end_machine:
    user_pick = choice_drink()
    if user_pick == True:
        end_machine = True
    else:
        beverage = MENU[user_pick]
        print(user_pick)
# TODO: 5. Process coins.
        sufficient_resources = check_resources()
        if sufficient_resources:
            quarters = int(input("Please insert coins.\n How many quarters?:"))
            insert_money = quarters * 0.25
            dimes = int(input("How many dimes?:"))
            insert_money = insert_money + dimes * 0.10
            nickles = int(input("How many nickles?:"))
            insert_money = insert_money + nickles * 0.05
            pennies = int(input("How many pennies?:"))
            insert_money = insert_money + pennies * 0.01
            #print(insert_money)
            if check_transaction(insert_money):
                make_drink()
