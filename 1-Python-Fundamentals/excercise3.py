a1 = int(input("Please enter the first angle: "))
a2 = int(input("Please enter the second angle: "))
a3 = int(input("Please enter the third angle: "))

if a1 <= 0 or a2 <= 0 or a3 <= 3:
    print("Angles smaller than 0 are not valid.")

elif (a1 + a2 + a3) != 180:
    print("The entered values are not valid.")

elif a1 == 90 or a2 == 90 or a3 == 90:
    print("The triangle is a right triangle.")

elif a1 > 90 or a2 > 90 or a3 > 90:
    print("The triangle is a obtuse triangle.")

else:
    print("The triangle is a acute triangle.")
