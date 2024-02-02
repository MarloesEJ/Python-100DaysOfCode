import random
import hangman_words
import hangman_art

chosen_word = hangman_words.word_list[random.randint(0,len(hangman_words.word_list)-1)]
display = []
running = True
lives = 6


for letter in chosen_word:
    display.append("_")

def showDisplay():
    print(' '.join(display))


print(hangman_art.logo)

showDisplay()

while running:
    guess_correct = False

    guess = input("make a guess: ").lower()

    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            guess_correct = True


    if not guess_correct:
        lives -= 1

    print(hangman_art.stages[lives])
    showDisplay()

    if "_" not in display:
        running = False
        print("You won!")
    elif lives == 0:
        running = False
        print("You lost!")

