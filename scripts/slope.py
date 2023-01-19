#pylint: disable=missing-docstring

while True:
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))

    PROD = str(y2 - y1) + "/" + str(x2 - x1)

    #pylint: disable=eval-used
    print(PROD + " = " + str(eval(PROD)))
