'''This script will calculate the slope of a line given two points.'''

def slope():
    '''This function performs the calculation'''
    x_1 = int(input("X1: "))
    y_1 = int(input("Y1: "))
    x_2 = int(input("X2: "))
    y_2 = int(input("Y2: "))

    prod = str(y_2 - y_1) + "/" + str(x_2 - x_1)

    #pylint: disable=eval-used
    return(prod + " = " + str(eval(prod)))

while True:
    OUT = slope()
    print(OUT)
