n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))
n3 = int(input("Please enter the third number: "))

nm = n1

if nm < n2:
    nm = n2

if nm < n3:
    nm = n3

print("The largest number is", nm)
