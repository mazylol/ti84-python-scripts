import os
from subprocess import call

from scripts.triangles.pythagorean import pythagorean

def handleTriangles():
    choice = input("1. Find Hyp (Pythag)\nQ. Quit\n")
    
    if (choice == "Q"):
        os._exit(0)
    elif (choice == "1"):
        _ = call('clear' if os.name == 'posix' else 'cls')
        pythagorean()
