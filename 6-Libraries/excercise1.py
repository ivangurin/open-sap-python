import random
import statistics


def gaussian_distribution():

    return [random.gauss(100, 10) for i in range(0, 1000)]


numbers = gaussian_distribution()

print("Mean:", statistics.mean(numbers))
print("Standard Deviation:", statistics.stdev(numbers))
