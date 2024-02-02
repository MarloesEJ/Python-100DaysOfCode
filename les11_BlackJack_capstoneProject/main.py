import random

cardValue = {"A": 11, "K": 10, "Q": 10, "J": 10, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}
cards = list(cardValue)
playerCards = []
playerScore = 0
dealerCards = []
dealerScore = 0

gameRunning = True
playerPlaying = False
dealerPlaying = False


def add_card(list_of_player):
    card_index = random.randint(0, 12)
    list_of_player.append(cards[card_index])
    return cardValue[cards[card_index]]


def you_lose():
    print(f"Your cards: {playerCards}, score = {playerScore}\n"
          f"Dealers first card: {dealerCards}. score {dealerScore}\n"
          f"You lose")


def you_win():
    print(f"Your cards: {playerCards}, score = {playerScore}\n"
          f"Dealers first card: {dealerCards}. score {dealerScore}\n"
          f"YOU WON!")


def game_over(player_plays):
    if dealerScore == 21 or playerScore > 21:
        you_lose()
        return 1
    elif playerScore == 21:
        you_win()
        return 1
    elif player_plays:
        return 0
    else:
        if dealerScore == playerScore:
            print(f"Your cards: {playerCards}, score = {playerScore}\n"
                  f"Dealers cards: {dealerCards}. score {dealerScore}\n"
                  f"it's a draw!")
        elif 21 > playerScore > dealerScore:
            you_win()
        else:
            you_lose()
        return 1


while gameRunning:
    wantToPlay = input("Do you want to play a game of blackjack, press 'y', else 'n': ")
    if wantToPlay == 'y':
        playerPlaying = True
        playerScore += add_card(playerCards)
        playerScore += add_card(playerCards)
        dealerScore += add_card(dealerCards)
        dealerScore += add_card(dealerCards)
    else:
        gameRunning = False

    while playerPlaying:
        if game_over(playerPlaying):
            playerPlaying = False
        else:
            print(f"Your cards: {playerCards} , current score = {playerScore}\nDealers first cards: {dealerCards[0]}")
            wantCard = input("Type 'y' to get another card, type 'n' to pass: ")
            if wantCard == 'y':
                playerScore += add_card(playerCards)
            else:
                dealerPlaying = True
                playerPlaying = False

    while dealerPlaying:
        if dealerScore < 17:
            add_card(dealerCards)
        else:
            game_over(playerPlaying)
            dealerPlaying = False
