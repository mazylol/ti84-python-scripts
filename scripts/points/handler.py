import os
from subprocess import call

from scripts.points.distance import distance
from scripts.points.slope import slope


def handlePoints():
    choice = input("1. Distance\n2. Slope\nQ. Quit\n")
    
    if (choice == "Q"):
        os._exit(0)
    elif (choice == "1"):
        _ = call('clear' if os.name == 'posix' else 'cls')
        distance()
    elif (choice == "2"):
        _ = call('clear' if os.name == 'posix' else 'cls')
        slope()
