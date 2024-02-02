import random

answer = random.randint(1, 100)


def give_lives(mode):
    if mode == "easy":
        return 10
    else:
        return 5


def check_answer(guess_check):
    if guess_check == answer:
        print(f"You got is the answer was {answer}")
        return 0
    elif guess_check > answer:
        print("Too high")
        return 1
    else:
        print("Too low")
        return 1


print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = give_lives(difficulty)
while lives > 0:
    print(f"You have {lives} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check = check_answer(guess)
    if check == 0:
        lives = 0
    elif lives == 1:
        print("You've run out of guesses,you lose.")
        lives = 0
    else:
        lives -= 1
