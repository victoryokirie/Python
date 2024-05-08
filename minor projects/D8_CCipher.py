##Caesar Cipher Project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >=26 or new_position <= -26:
                new_position = new_position % 26
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"The {cipher_direction}d text is {final_text}")

restart = True

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'Yes' if you want to continue. Otherwise, type 'No' to exit.\n").lower()

    if result == "no":
        restart = False
        print("Goodbye")

