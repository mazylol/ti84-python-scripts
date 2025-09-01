'''This script finds the hypothenuse of a right triangle given the other two sides.'''

from math import sqrt

def pythagorean():
    while True:
        a = int(input("Side A: "))
        b = int(input("Side B: "))

        prod = (a ** 2) + (b ** 2)
        root = sqrt(prod)

        print(root)
