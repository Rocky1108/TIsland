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
/______/______/______/______/______/______/______/______/______/______/[Rakesh]
*******************************************************************************''')
print("Welcome to Treasure Island, your mission is to find the treasure")
print("Choose your path carefully or else you will die.")
first = input("Which way you want to go?left or right? ").lower()
if first == "left":
    print("You got lucky,you live")
    second = input("Wooh There's a lake, do you wanna catch fish for food?yes or no").lower()
    if second != "no":
      print("There's a crocodile in the lake, Game Over ")
    else :
        print("You are one son of a bitch, you live.")
        third = input("You found  a mysterious box, do you want to open it? y or n").lower()
        if third != "n":
          print("There's a map.This will guide you to the treasure")
          door = input("Which door you want to open,red or white")
          if door == "red":
               print("There's the treasure, you found it.")
          else:
                  print("There's a beast.You die. GAME OVER")

else:
    print(" BOOM there's a bomb.Game Over.")
