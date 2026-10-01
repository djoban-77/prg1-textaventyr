# The Lost Temple 

print("THE LOST TEMPLE")

name = input("what is your name? ")
print(f"welcome, {name}! ")
print(f"{name}, you are about to begin a strange adventure")
print(f"good luck, {name}! ")

print("You are exploring a mysterious forest when you discover an incient temple")
choice1 = input("Do you ente the temple or leave? ")

if choice1 == "enter":
    print("You step inside thee temple.")
    print("Suddenly the ground begins to shake! ")

    choice2 = input("Do you go in deeper into the temple or go back? ")

    if choice2== "deeper":
       print("You run depper into the temple.")
       print("You find a strange glowing portal.")

       choice3 = input("Do you enter the portal or stay? ")

       if choice3 == "enter":
          print("You step through the portal.")
          print("Everything goes dark.")
          print("When you open your eyes, you realise you are in an")
          print("ALTERNATIVE UNIVERSE! ")

          print(f"{name}, you discover this universe is different from your own.")
          print("You have the power to change history.")

          choice4 = input("Do you change history and become a suprem overlord,"  "or do nothing? ")

          if choice4 =="change history":
             print("You decide to change history.")
             print("You use your knowledge to alter important events. ")
             print("Your influence grows stronger and stronger. ")
             print(f"congratulation. {name}! ")
             print("You become the SUPREME OVERLORD of the alternative universe!")

          elif choice4 == "do nothing":
               print("You decide yhat changing hiostpry is to dangerous.")
               print("You leave history untouched.")
               print(f"{name}, you begin searching for a way back home.")
               print("THE END, history Preserved.")

          else:
               print("You hestite for too long.")
               print("The portal disappears.")
               print(f"{name}, you are trapped in the altenative universer forever.")
               print("THE END, lost forever.")
       else:
            print("You decide not to enter the portal.")
            print("You turn around, but the temple has changed.")
            print("You can't find your way back home.")
            print(f"{name}, you are lost inside the temole forever ")
            print("THE END, lost in the temple forever.")
    
    elif choice2 == "back":
        print("You try to return to the entrence")
        print("But every hallway look exactly the same.")
        print("You become completeöy lost and cannon't find a way home.")

        print("Sunddenly, you discover a hidden room.")
        print("Inside is a strange glowing portal.")

        choice3 = input("Do you enter or stay? ")

        if choice3 == "enter":
            print("You enetr the portal.")
            print("You have been transportade to an alternative universe.")

            choice4 = input("Do you change history and become the supreme overlord,"  "or do nothing? ")

            if choice4 == "change history":
                print(f"{name}, you change history and become the supreme overlord.")
                print("THE END, supreme overlord.")

            elif choice4 == "Do nothing":
                print(f"{name}, you decide not to enterfere with history. ")
                print("You spend the rest of your life searching for a way home.")
                print("THE END, history reserved.")

            else:
                print("You couldn't make a decision.")
                print("THE END, lost in time.")
        else:
            print(f"{name}. you stay in the temple.")
            print("You never fing the way home.")
            print("THE END, lost for ever.")
    else:
        print("You didn't make a clear decision.")
        print(f"{name}, you leave the temple and return to the forest.")
        print("THE END, the safe escape.")
else:
    print("You decide not to enter the temple.")
    print("You return home safely.")
    print(f"well done, {name}! sometimes the safest choice is the best one.")
    print("THE END, safe at home.")
        
                     

         