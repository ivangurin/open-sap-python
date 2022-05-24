
numbers = []

with open("numbers.txt", "r") as file:

    lines = file.readlines()

    for line in lines:
        line = line.strip()
        numbers.append(int(line))


with open("even_numbers.txt", "w") as file:

    for number in numbers:

        if number % 2 == 0:

            file.write(str(number) + "\n")

print("List of even numbers created!")
