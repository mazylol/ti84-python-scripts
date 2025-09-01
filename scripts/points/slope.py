'''This script will calculate the slope of a line given two points.'''

def slope():
    while True:
        x_1 = int(input("X1: "))
        y_1 = int(input("Y1: "))
        x_2 = int(input("X2: "))
        y_2 = int(input("Y2: "))

        prod = str(y_2 - y_1) + "/" + str(x_2 - x_1)

        #pylint: disable=eval-used
        print(prod + " = " + str(eval(prod)))
