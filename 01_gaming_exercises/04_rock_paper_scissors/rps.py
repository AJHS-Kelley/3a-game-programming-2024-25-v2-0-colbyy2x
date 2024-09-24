# ROCK,PAPER, SCISSORS by Jacolby Allen, v0.0

# MODULE IMPORTS 
import random

# DATA STRUCTURES -- PLAYER
playerscore = 0
playerName = "Test Player"
playerChoice= None

#DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please type your name and press enter.\n")
print(f"Hellow {playerName}!\n")
isCorrect = input("Is that corretc? Type yes or no and press enter.\n").lower()

# .lower() can turn ALL input into lowercase.
# .lower() can turn All input into UPPERCASE.

if isCorrect == "Yes":
    print(f"ok {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type your name and press enter.\n"
                       
# THE RULES using MULTI-LINE STRINGS
print(f"""
Welcome, {playername} to the rock, paper, scissors Robot!
It's Time to play rock, paper, scissors!

You will play against the CPU, The first player to score 5 points win.
You will select from ROCK, PAPER, or SCISSORS.
The CPU will select ROCK, PAPER, or SCISSORS at random.
      
1) ROCK BEATS SCISSORS 
2) SCISSORS BEATS PAPER 
3) PAPER BEATS ROCK
""")

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS 
"""
Anything in between the sets of double-quotes is just ignored.
If you need to write large comments. it's easier to use multi-line strings than
putting a # in front of 15 different lines
"""

# MAIN GAME LOOP
while playerscore < 5 and cpuScore < 5:
    print(f"{playerName}you have {playerName}points.\nThe CPU has { cpuScore}points.\n")
    playerChoice = input("Please enter rock,paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print( "You are not following directions. PLease try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")

# let cpu select choice at random.
cpuChoice= random.randint(0,2) # randomly select 0,1, or 2
if cpuChoice ==0:
    cpuChoice="rock"
elif cpuChoice == 1:
    cpuChoice == "scissors"        
elif cpuChoice == 2:
    cpuChoice == "paper"
else:
    print("Unable to determine CPU choice.\nPlease restart. \n")
    exit()
    # print(f"CPU Choice: {cpuChoice}")
    
    # compare player choice to cpu choice
    if playerChoice=="rock" and cpuChoice == "paper"
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The Cpu wins a point.\n")
        cpuScore +=1
    elif playerChoice == "rock" and cpuChoice ==" scissors":
        # PLAYER WINS
        print(f" The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerscore +=1
    elif playerChoice == "rock" abd cpuChoice == "rock":
        # DRAW                                                      