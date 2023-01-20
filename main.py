import os

print("Welcome to the jungle!")
print("We've got fun and games!")

print("Make a choice:")

choice = input("1. Algebra\n2. Geometry\nQ. Quit\n")

if (choice == "Q"):
    os._exit(0)
