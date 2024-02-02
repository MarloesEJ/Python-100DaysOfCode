alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
running = True


def caesar(text, shift, direction):
    new_text = []
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            new_text.append(alphabet[(alphabet.index(char)+shift)% len(alphabet)])
        else:
            new_text.append(char)
    print(f"The encoded text is {''.join(new_text)}")


while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    going = input("want to go on? yes of no:\n")
    if not going.lower() == "yes":
        running = False
