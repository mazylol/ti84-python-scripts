#pylint: disable=missing-docstring

from math import sqrt

while True:
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))

    prod = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    root = sqrt(prod)

    print(root)
