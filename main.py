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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

he1 = input("Choose left or right?").lower()

if he1=="left":
   he2=input("Do you want to swim or not: ").lower()
   if he2=="not":
     he3=input("Choose which door: ").lower()
     if he3=="blue":
       print("Game over!")
     elif he3=="red":
       print("Game Over1!")
     elif he3=="yellow":
       print("You win!!!")
     else:
       print('Why u lose')
   else:
     print("You lose")
else:
  print("dufvcuy")
     





     
# if he1 == "left":
#    he2 = input("Choose to swim or wait : ").lower()
#    if he2 == "wait":
#     he3 = input("Which door do u wanna choose for your death! :").lower()
#     if he3 == "blue":
#       print("You Win!")
#     elif (he3 == "red") :
#       print("Game over")
#     elif (he3 == "yellow"):
#       print("shfvbs")
#     else:
#       print("Gaywgfi")
#    else:
#       print("Game over")
# else:
#   print("Game Over")
# he2 = input("Choose to swim or wait")
# he3 = input("Which door? do you choose")
# he4 = he1.lower()
# he5 = he2.lower()
# he6 = he3.lower()

# if he4 == right:
#   print("Game Over")
# elif he5 == swim:
#   print("Game Over")
# else:
#   print("Choose one")