import random
import math

within = 0

for _ in range(0, 10000):

    x = random.random()
    y = random.random()

    if x ** 2 + y ** 2 < 1:
        within += 1

pi = within / 10000 * 4

print("Calculated value of π:", pi)
print("Value of π from math library:", math.pi)
print("Difference:", pi-math.pi)
