import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
amount_letters = int(input("How many letters would you like in your password?\n"))
amount_numbers = int(input("How many numbers would you like?\n"))
amount_special = int(input("How many special symbols would you like?\n"))

password = []

for letter in range(1,amount_letters+1):
    password.append(random.choice(letters))
for number in range(1, amount_numbers+1):
    password.append(random.choice(numbers))
for special in range(1, amount_special+1):
    password.append(random.choice(symbols))

random.shuffle(password)
password = ''.join(str(e) for e in password)

print(f"your password is: {password}")
