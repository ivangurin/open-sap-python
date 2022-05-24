alphabet = "abcdefghijklmnopqrstuvwxyz"

shift = input("Please enter the number of places to shift: ")

if shift.isdecimal():

    shift = int(shift)

    if 0 <= shift <= 25:

        text = input("Please enter a sentence: ")

        result = ""

        for letter in text.lower():

            if letter in alphabet:

                index = alphabet.find(letter)

                index += shift

                if index > 25:
                    index = index % 26

                result += alphabet[index]

            else:

                result += letter

        print("The encrypted sentence is:", result)

    else:

        print("You need to enter a number between 0 and 25!")

else:

    print("You need to enter a number between 0 and 25!")
