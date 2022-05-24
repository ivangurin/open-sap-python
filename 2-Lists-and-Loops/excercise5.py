for value in range(1, 101):

    result = ""

    if value % 3 == 0:
        result = "Fizz"
    
    if value % 5 == 0:
        result += "Buzz"

    if result == "":
        result = str(value)

    print(result)