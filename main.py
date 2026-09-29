# The Lost Temple 

print("THE LOST TEMPLE")

name = input("what is your name? ")
print(f"welcome, {name}! ")
print(f"{name}, you are about to begin a strange adventure")
print(f"good luck, {name}! ")

print("You are exploring a mysterious forest when you discover an incient temple")
choice1 = input("Do you ente the temple or leave? ")

if choice1 == "enter":
    print("You step inside thee temple")
    print("Suddenly the ground begins to shake! ")

choice2 = input("Do you go in deeper into the temple or go back? ")

if choice2== "deeper":
    print("You run depper into the temple")
    print("You find a strange glowing portal")

elif choice2 == "back":
    print("You try to return to the entrence.")
    print("But every hallway looks exactly the same.")
    print("You become completely lost and cannot find the way back.")

    print("Suddenly you find a hidden room.")
    print("Inside is a strange glowing portal.")

choice3 = input("Do you enter the portal or stay? ")

if choice3 == "enter":
    print("You step through the portal")
    print("Everything goes dark")
    print("When you open your eyes, you realise you are in an")
    print("ALTERNATIVE UNIVERSE! ")

print(f"{name}, you discover this universe is different from your own.")
print("You have the power to change history")

choice4 = input("Do you change history and become a suprem overlord,"  "or do nothing? ")

if choice4 =="change history":
    print("You decide to change history")
    print("You use your knowledge to alter important events. ")
    print("Your influence grows stronger and stronger. ")
    print(f"congratulation. {name}! ")
    print("You become the SUPREME OVERLORD of the alternative universe!")

elif choice4 == "do nothing":
    print("You decide not to interfere with  history.")
    print("You leave history untouched.")
    print("You spend your life searching for a way home")
    print("THE END, history Preserved")

else:
    print("You couldn't make a decision.")
    print("THE END, lost in time")

