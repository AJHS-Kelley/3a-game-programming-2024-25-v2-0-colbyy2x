# Demon Slayer, JacOlby Allen, v0.0

import random
import time

def displayIntro():

    print('One random night you hear something outside')
    print('You take a look outside and see a dark shadowy figure flash infront of you')
    print('You start to run but only have three paths and one weapon to choose from')
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
        print('Lights are flickering on and off ')
        time.sleep(2)
        print("")

    friendlyPath = random.randint(1)
    DeadlyPath = random.randint(2)
    
    if chosenPath == str(DeadlyPath):
        print('You have ran into a building with more demons')

    else:
        print('You get eaten by demons')
        print('Game over ')
    
    if chosenPath == str(friendlyPath):
        print('You have made it away from the demon ')

    else:
        print('You bleed out and become a demon')
        print('Game over')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    PathNumber = choosePath()
    checkPath(PathNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()