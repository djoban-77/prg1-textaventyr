# The Lost Temple 

print("THE LOST TEMPLE")

name = input("what is your name? ")
print(f"welcome, {name}! ")
print(f"{name}, you are about to begin a strange adventure")
print(f"good luck, {name}! ")

#start of the story
print("You are exploring a mysterious forest.")
print("You discover an incient temple.")

choice1 = input("Do you ente the temple or leave? ")

if choice1 == "enter":
    print("You enter the temple.")
    print("Suddenly the entrance disappears! ")

    #The player finds a key
    print("You look around and find a strange golden key.")
    has_key = True
    print("You put the key in your pocket.")

    choice2 = input("Do you go in deeper into the temple or go back? ")

    if choice2== "deeper":
       print("You walk depper into the temple.")
       print("You discover a mysterious door.")

       if has_key:
           print("The golden key fits perfectly into the door! ")

           choice3 = input("Do you use the key or leave the door?")

           if choice3 == "use the key":
            print("You unlock the mysterious door.")
            print("Behind it, you discover a glowing portal.")
            
            choice4 = input("Do you enter the portal or stay? ")

           if choice4 =="enter":
              print("You enter the portal.")
              print("Everything goes dark... ")
              print("You wake up in an alternative universe!. ")
              print(f"{name}, you discover that this universe has complete different history.")

              choice5 = input("Do you change history,do nothing" "or find a way home? ")

              if choice5 == "change history":
                  print("You decide to change history.")
                  print("You use your knowledge of history to change the important events.")
                  print(f"{name}, ypour power grows untill you become supreme overlord! ")
                  print("THE END, supreme overlord.")
            
              elif choice5 == "do nothing":
                  print("You decide not to enterfere with history.")
                  print(F"{name}, you spend your time searching for a way back home.")
                  print("THE END, history preserved.")
             
              elif choice5 == "find a way home":
                  print("You search the alternative universe.")
                  print("You discover another portal.")
                  print(f"{name}, you step through it and return to your original universe! ")
                  print("THE END, home again.")

              else:
                 print("That was not a valid choice")
                 print("THE END, lost in time.")
               
           elif choice4 == "stay":
               print("You decide not toi enter the portal.")
               print(f"{name}, you become trapped inside the ancient temple.")
               print("THE END, lost in the temple.")
    
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
        
                     

         