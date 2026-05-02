print("Welcome to the Game of Choices!!")
print("You are a Queen of an empire. You have to defeat the evil King and find the treasure. You have to make choices to defeat the King and get the treasure. Good luck!")
print("You're in the castle. You see a two doors. left and right. Which door will you choose?")
choice1 = input("Type 'left' or 'right' to choose a door: \n")
if choice1 == "left":
  print("You're in the room of the King. You see a sword and a grenade. Which one will you choose?")
  choice2 = input("Type 'sword' or 'grenade' to choose a weapon: \n")
  if choice2 == "sword":
    print("You have attacked the King with the sword and defeated him. You see 4 caskets. One of them has the key to the treasure box room. Which casket will you choose?")
    choice3 = input("Type 1, 2, 3 or 4 to choose a casket: \n")
    if choice3 == "1" or choice3 == "2" or choice3 == "4":
      print("You chose the wrong casket, the guards caught you and killed you. Game over!")
    elif choice3 == "3":
      print("You found the Key! You are now in the treasure box room.")
      print("You see a gold box, silver box and bronze box. Which one will you choose?")
      choice4 = input("Type 'gold', 'silver', 'bronze' to choose a box: \n")
      if choice4 == "gold" or choice4 == "silver":
        print("You chose the wrong box, a poisonous gas was released from the box and you died. Game over!")
      else:
        print("You chose the right box! You found the Treasure! You win!")
  else:
    print("You chose the grenade, which killed both the you and the King. Game over!")
  
else: 
  print("You chose the right door. You are attacked by the guards and died. Game over!")
