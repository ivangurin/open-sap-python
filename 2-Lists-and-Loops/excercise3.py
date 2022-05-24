rows = int(input("Please enter the number of rows in the matrix: "))
cols = int(input("Please enter the number of columns in the matrix: "))

matrix = []

print("Enter the matrix values:")

for row in range(rows):

    matrix_row = []

    for col in range(cols):

        value = int(input("Please enter the value of row " + str(row+1) + " of column " + str(col+1) + ": "))

        matrix_row.append(value)

    matrix.append(matrix_row)

for matrix_row in matrix:

    print("Sum of row: ", sum(matrix_row))
