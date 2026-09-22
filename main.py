# The Lost Temple 

print("THE LOST TEMPLE")

name = input("what is your name? ")
print(f"welcome, {name}! ")
print(f"{name}, you are about to begin a strange adventure")
print(f"good luck, {name}! ")

print("You are exploring a mysterious forest when you discover an incient temple")
choice1 = input("Dp you ente the temple or leave? ")

if choice1 == "enter":
    print("You step inside thee temple")
    print("Suddenly the ground begins to shake! ")

choice2 = input("Do you run deeper into the temple or run back? ")

if choice2== "deeper":
    print("You run depper into the temple")
    print("You find a strange glowing portal")

choice3 = input("Do you enter the portal or stay? ")

if choice3 == "enter":
    print("You step through the portal")
    print("Everything goes dark")
    print("When you open your eyes, you realise you are in an")
    print("ALTERNATIVE UNIVERSE! ")

print(f"{name}, you discover this universe is different from your own.")
print("You have the power to change history")

choice4 = input("Do you change history and become a suprem overlord,"  "or do nothing ")