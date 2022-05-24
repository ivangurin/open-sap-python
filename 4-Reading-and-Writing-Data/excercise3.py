
products = []

with open("invoice_data.txt", "r") as file:

    lines = file.readlines()

    for line in lines:

        line = line.strip()

        data = line.split()

        product = (data[0], int(data[1]), float(data[2]))

        products.append(product)

for product in products:

    print(f"{product[0]:15s}{product[1]:3d}{product[2]:7.2f}{product[1]*product[2]:8.2f}")
