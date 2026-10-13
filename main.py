# The Lost Temple 

print("THE LOST TEMPLE")

name = input("what is your name? ")
print(f"welcome, {name}! ")
print(f"{name}, you are about to begin a strange adventure")
print(f"good luck, {name}! ")

#start of the story
print("You are exploring a mysterious forest.")
print("You discover an incient temple.")

choice1 = input("Do you enter the temple or leave? ")

if choice1 == "enter":
    print("You enter the temple.")
    print("Suddenly the entrance disappears! ")

    #The player finds a key
    print("You look around and find a strange golden key.")
    has_key = True
    print("You put the key in your pocket.")

    choice2 = input("Do you go in deeper or stay? ")

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
           else:
               print("That was not a valid choice.")
               print("THE END.")
       
       elif choice3 == "Leave":
           print("You decide to leave the door alone. ")
           print("You turn around, but the temple has changed. ")
           print(f"{name}, you cannot find your way back. ")
           print("LOST FOREVER.")

       else:
           print("That was not a valid choice.")
           print("THE END.")
    
    elif choice2 == "stay":
        print("You decide yo stay near the entrence")
        print("After some time, the entrence reappers.")
        print(f"{name}, you escape the temple safely.")
        print("THE END, safe escape")

    else:
        print("That was not a valid choice.")
        print("THE END.")

else:
    print("You decide not to enter the temple.")
    print(f"{name}, you return home safely.")
    print("THE END, safe at home. ")
        
                     

         