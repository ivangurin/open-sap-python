ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt_letter(letter: str, shift: int) -> str:

    if not letter.isalpha():
        return letter

    index = ALPHABET.find(letter)

    index += shift

    index %= 26

    return ALPHABET[index]


def calculate_shifts(letter: str) -> int:

    return ALPHABET.find(letter)


def encrypt_text(text: str, key: str) -> str:

    text = text.lower()
    key = key.lower()
    counter = 0

    result = ""

    for index in range(len(text)):


        counter += 1

        if counter > len(key):
            counter -= len(key)
        
        letter = text[index]

        shift = calculate_shifts(key[counter-1])

        encrypted_letter = encrypt_letter(letter, shift)

        result += encrypted_letter

    return result

input_text = input("Which text should be encrypted: ")
input_key = input("Which keyword should be used? ")

print(encrypt_text(input_text, input_key))
