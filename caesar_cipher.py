alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
signals = [" ", ",", "!", "?", "/", ".", "\"", "%", "(", ")"]

def caesar_cipher (call_text, shift_value, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_value += -1
    if shift_value > 26:
        shift_value = shift_value%26
    for letter in call_text:
        if letter in signals:
            final_text += letter
        else:
            position = alphabet.index(letter)
            new_pos = position + shift_value
            new_letter = alphabet[new_pos]
            final_text += new_letter
    print(f"Here's the {cipher_direction}d result: {final_text}\n")

end_program = False
while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") .lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(cipher_direction=direction, call_text=text, shift_value=shift)

    restart = input("Type '\Yes' if you want to go again. Otherwise type 'No'.\n") .lower()
    if restart == "no":
        end_program = True
        print(f"Goodbye.")
