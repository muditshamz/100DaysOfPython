print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



while game_over == False:
  action1 = input("Type your first move? use 'left' or 'right' \n")
  if action1 == "left":
    action2 = input("you want to 'swim' or 'wait'\n")
    if action2 == "wait":
      action3 = input("Which door? Red, Blue, Yellow or something else?\n")
      if action3 == "Yellow":
        print("You win!")
        break
      elif action3 == "Red":
        print("Burnt by fire \n Game Over!")
        break
      elif action3 == "Blue":
        print("Eaten by beasts \n Game Over!")
        break
      else:
        print("Game Over.")
        break
    else:
      print("Attacked by trout. \n Game Over.")
      break
  else:
    print("Fall into a hole.\n Game Over.") 
    break
