import os
from subprocess import call

from scripts.quads.prove.parallelogram import parallelogram

def handleQuads():
    choice = input("1. Prove Parallelogram\nQ. Quit\n")
    
    if (choice == "Q"):
        os._exit(0)
    elif (choice == "1"):
        _ = call('clear' if os.name == 'posix' else 'cls')
        parallelogram()
