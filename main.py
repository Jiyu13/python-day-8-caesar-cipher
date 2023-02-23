from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:

        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


is_end_game = False
while not is_end_game:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 25:
        shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # TODO-12: Can you figure out a way to ask the user if they want to restart the cipher program?
    # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    # Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    if play_again == "no":
        is_end_game = True
        print("bye")
