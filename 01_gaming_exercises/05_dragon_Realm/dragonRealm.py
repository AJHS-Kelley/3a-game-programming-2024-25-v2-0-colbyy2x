# Demon Slayer, JacOlby Allen, v0.0

import random
import time
import datetime 
pickWeaponUp = " yes or no"
fightBack = "yes or no "

# SAVING DATA TO A FILE 
# STEP 1-- Create thefile name to use.
logFileName="DraginRealmLog" + str(time.time()) + ".txt"
#logFileName = "DraginRealmLog.txt"
# Example: dragonRealmLog1132AM.txt

# STEP 2 -- CREATE / OPEN THE FILE TO SAVE THE DATA
saveData = open(logFileName, "a")
#FILE MODES 
#"X" CREATES FILE, IF FILE EXIST, EXIT WITH ERROR MESSAGE
#"W" CREATE FILE, IF FILE EXIST, ERASE AND OVERWRITE FILE CONTENTS
# "A" CREATE FILE, IF FILE EXIST, APPEND DATA TO THE FILE.

saveData.write("GAME STARTED"+ " "+ str(datetime.datetime.now())+ "\n")
def displayIntro():

    print('One random night you hear something outside')
    print('You take a look outside and see a dark shadowy figure flash infront of you')
    print('You start to run but only have three paths and one weapon to choose from')
    print('If you dont choose the right path you will not have the option to fight back')
    print('sooo.......')
    print('Choose wisely.')
    print()

def choosePath():
    path = ''
    while path != '1' and path != '2' and path != '3':
        print('Which path will you choose ? (1,2, or 3)')
        path = input()
    return path

def checkPath(chosenPath):
    if chosenPath != 1:
        print('You approach an alley')
        time.sleep(2)
        print('Street lights are flickering on and off ')
        time.sleep(2)
        print("")
    else:
        chosenPath = 2
        print("You have reached a house")
        time.sleep(2)
        print("You open the door, you are now faced with more demons")
        time.sleep(2)
      


    friendlyPath = random.randint(1,2)
    DeadlyPath = random.randint(2,3)
    closet = ''
    
    if chosenPath == str(DeadlyPath):
        print('You have ran into a building with more demons')
        print('You can run into the closet')
        time.sleep(2)
        print('Would you like to hide in the closet?')
        print('Yes or no?')
        closet = input()
        print("You run into the closet")
        time.sleep(2)
        print("There is a sowrd in there with you.")
        time.sleep(2)
        print("Would you like to pick it up? Yes or no")
        time.sleep(2)
        pickWeaponUp = input()
        print("You have picked the weapon.")
        time.sleep(2)
        print("You have the option to fight back. Would you like to? Yes or no?")
        fightBack = input()
        print(" Congrats You have killed the demon")
    else:
        print('You get eaten by demons')
        print('Game over ')
    
    if chosenPath == str(friendlyPath):
        print('You have made it away from the demon ')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    PathNumber = choosePath()
    checkPath(PathNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()

playAgain = 'no'
print("Thank you for playing")

# CLOSE THE FILE 
saveData.write(r"END OF GAME LOG\N\N")
saveData.close()
