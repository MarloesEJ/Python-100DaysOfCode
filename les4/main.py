import random

choisePC = random.randint(0, 2)

choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

listOfMoves = [rock, paper, scissors]
listOfMoveNames = ["rock", "paper", "scissors"]


print(f"the player choose {listOfMoveNames[choise]} {listOfMoves[choise]}\n the pc choose {listOfMoveNames[choisePC]} {listOfMoves[choisePC]}")

if (choise == 0 and choisePC == 0) or (choise == 1 and choisePC == 1) or (choise == 2 and choisePC == 2):
    print("its a draw")
elif (choise == 0 and choisePC == 2) or (choise == 1 and choisePC == 1) or (choise == 2 and choisePC == 1):
    print("You won!")
else:
    print("You lost")