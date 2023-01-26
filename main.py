import os
from scripts.points.handler import handlePoints

print("Welcome to the jungle!")
print("We've got fun and games!")

print("Make a choice:")

choice = input("1. Points\n2. Quads\n3. Triangles\nQ. Quit\n")

if (choice == "Q" or choice == "q"):
    os._exit(0)
elif (choice == "1"):
    handlePoints()
