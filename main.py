import os
from subprocess import call
from scripts.points.handler import handlePoints
from scripts.quads.prove.handler import handleQuads
from scripts.triangles.handler import handleTriangles

print("Welcome to the jungle!")
print("We've got fun and games!")

print("Make a choice:")

choice = input("1. Points\n2. Quads\n3. Triangles\nQ. Quit\n")

if (choice == "Q" or choice == "q"):
    os._exit(0)
elif (choice == "1"):
    _ = call('clear' if os.name == 'posix' else 'cls')
    handlePoints()
elif (choice == "2"):
    _ = call('clear' if os.name == 'posix' else 'cls')
    handleQuads()
elif (choice == "3"):
    _ = call('clear' if os.name == 'posix' else 'cls')
    handleTriangles()
