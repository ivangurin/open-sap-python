qunatity = int(input("Please enter an initial stock level: "))
monthes = int(input("Please enter the number of month to plan: "))

plan = []

for month in range(monthes):
    month_plan = int(input("Please enter the planned sales quantity for month " + str(month+1) + ": "))
    plan.append(month_plan)

print("The resulting production quantities are:")

for month in range(monthes):

    qunatity = qunatity - plan[month]

    if qunatity > 0:
        need = 0
    else:
        need = -1 * qunatity
        qunatity = 0

    print("Production quantity month", month+1, "-", need)
