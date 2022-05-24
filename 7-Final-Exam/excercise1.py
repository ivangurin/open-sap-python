
import random


def word_list() -> list:

    words = []

    with open("7-Final-Exam/5_letter_words.txt", "r") as file:

        lines = file.readlines()

        for line in lines:
            line = line.strip()
            words.append(line)

    return words


def random_word(words: list) -> str:

    return random.choice(words)


def is_real_word(word: str, words: list):

    if word in words:
        return True

    return False


def check_guess(guess_word: str, secret_word: str):

    local_secret_word = secret_word

    result = ""

    for index in range(0, len(guess_word)):

        if guess_word[index] in local_secret_word:

            if guess_word[index] == secret_word[index]:
                result += "X"
            else:
                result += "O"

            local_secret_word = local_secret_word.replace(guess_word[index], " ", 1)

        else:

            result += "_"

    return result


def next_guess(words: list) -> str:

    while True:

        guess_word = input("Please enter a guess: ")

        if guess_word.lower() in words:
            return guess_word.lower()
        
        print("That's not a real word!")


def play():

    words = word_list()

    secret_word = random_word(words)

    for attempt in range(6):

        guess_word = next_guess(words)

        print(check_guess(guess_word, secret_word))

        if guess_word == secret_word:
            print("You won!")
            break

        if attempt == 5:
            print("You lost!")
            print(f"The word was: { secret_word }")

play()
