import random
import art
import data

score = 0
playing = True

print(art.logo)


def get_random_account():
    return random.randint(0, len(data.data))


def compare(choose, option1, option2):
    if choose == "a":
        if data.data[option1]['follower_count'] >= data.data[option2]['follower_count']:
            return 1
        else:
            return 0
    else:
        if data.data[option2]['follower_count'] >= data.data[option1]['follower_count']:
            return 1
        else:
            return 0


while playing:
    prompt1 = get_random_account()
    prompt2 = get_random_account()
    print(f"Compare A: {data.data[prompt1]['name']}, from {data.data[prompt1]['description']}, from {data.data[prompt1]['country']}")
    print(art.vs)
    print(f"Against B: {data.data[prompt2]['name']}, a {data.data[prompt2]['description']}, from {data.data[prompt2]['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if compare(guess, prompt1, prompt2) == 1:
        score += 1
        print("\n"*1000)
        print(art.logo)
        print(f"You're right! Current Score: {score}")
    else:
        playing = False

print(f"Sorry, that's wrong. Final score: {score}")
