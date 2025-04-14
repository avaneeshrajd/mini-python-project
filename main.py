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
print("There is blocked road ahead due to landslide.")
print('Now,You\'ve two choices left either take "Left" or take "Right".')
Direction= input("What was your choice choose carefully.\n").lower()
if Direction== "left":
  print("Oh! You\'ve reached to river.")
  print("There is a island in the river in which you will be able to find you're treasure.")
  print('Now as the boat is coming in some time.You\'ve two choices left either type "wait" to wait for boat or "swim" to swim through the river.')
  choice_2=input('What you want to do either "Wait" or "Swim".\n').lower()
  if choice_2 == "wait":
    print('you\'ve reach to the island where the treasure is hidden.') 
    print('Now there is three room of different color of doors in which only one of them has treasure.')
    print('The three door is of color "red","blue" and "yellow".')
    choice_3=input('Which door you want to choose type color of that door.\n').lower()
    if choice_3 == "yellow":
      print("You Win!!!!!")
      print("congratulations!!!, Now you have the largest ever treasure anyone have....")
    elif choice_3 == "red":
      print("Oh my God!!!")
      print("You have choosen wrong door. The room is covered with fire. Due to which you burned out. ")
      print("Game Over!!!!")
    elif choice_3 == "blue":
      print("Oh my God!!!")
      print("You have choosen wrong door. This room is filled with lots of deadly animal which was reason of your death.")
      print("Game Over!!!!")
    else:
      print("You have entered wrong choice..")
      print("Game Over!!!!")
  else:
    print("In the river there is a lot of deadly sharks...Game Over!!!")
else:
  print("There is a cheetah in front of you...Game Over!!!")
  
  
