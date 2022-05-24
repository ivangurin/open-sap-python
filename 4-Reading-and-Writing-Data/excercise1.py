
numbers = []

with open("numbers.txt", "r") as file:
    
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        numbers.append(int(line))

numbers.sort(reverse=True)

for number in numbers[0:3]:
    print(number)
