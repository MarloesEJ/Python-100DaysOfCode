import replit

auction = {}
running = True


def add_bet(key, value):
    auction[key] = value


def check_highest_bet():
    highest_bet = 0
    for bet in auction:
        if highest_bet < auction[bet]:
            highest_bet = auction[bet]
            highest_bidder = bet
    print(f"The highest bid is {highest_bet} done by {highest_bidder}")


while running:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bet(name, bid)
    keepGoing = input("Is there someone else who wants to place a bid, yes or no: ").lower()
    if keepGoing == "no":
        running = False
    else:
        replit.clear()

check_highest_bet()

