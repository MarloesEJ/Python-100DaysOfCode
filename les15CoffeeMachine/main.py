import data

running = True
resources = ["water", "milk", "coffee"]


def get_report():
    print(f"Water: {data.resources['water']}ml\n"
          f"Milk: {data.resources['milk']}ml\n"
          f"Coffee: {data.resources['coffee']}g\n"
          f"Money: ${data.resources['money']}")


def check_resources(coffee, resource):
    if data.coffees[coffee][resource] > data.resources[resource]:
        print(f"Sorry there is not enough {resource}")
        return False
    else:
        return True


def collect_coins(coffee):
    total = 0
    total += int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.1
    total += int(input("how many nickels?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    if total > data.coffees[coffee]['cost']:
        change = total - data.coffees[coffee]['cost']
        print(f"Here is ${change:.2f} in change")
        return True
    elif total < data.coffees[coffee]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def use_resources(coffee):
    data.resources['water'] -= data.coffees[coffee]['water']
    data.resources['milk'] -= data.coffees[coffee]['milk']
    data.resources['coffee'] -= data.coffees[coffee]['coffee']


while running:
    whatCoffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if whatCoffee == "off":
        running = False
    elif whatCoffee == "report":
        get_report()
    elif (check_resources(whatCoffee, resources[0]) and
          check_resources(whatCoffee, resources[1]) and
          check_resources(whatCoffee, resources[2])):
        print(f"your {whatCoffee} costs: ${data.coffees[whatCoffee]['cost']}\nPlease insert coins")
        if collect_coins(whatCoffee):
            data.resources['money'] += data.coffees[whatCoffee]['cost']
            use_resources(whatCoffee)
            print(f"here is your {whatCoffee}. Enjoy!")
