# ROCK,PAPER, SCISSORS by Jacolby Allen, v3.0

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
def playerName(): # Function Signature -- name of function, (arguments if any)
    playerName = input("Please type your name and press enter.\n")
    print(f"Hello {playerName}!\n")
    isCorrect = input("Is that corretc? Type yes or no and press enter.\n").lower()
    if isCorrect == "Yes":
        print(f"ok {playerName}, let's play Rock, Paper, Scissors!\n")
    else:
        playerName = input("Please type your name and press enter.\n")
    return playerName

# CALLING THE FUNCTION 
playerName = playerName()                       

# THE RULES using MULTI-LINE STRINGS
def rules():
    print(f"""
    Welcome, {playerName} to the rock, paper, scissors Robot!
    It's Time to play rock, paper, scissors!

    You will play against the CPU, The first player to score 5 points win.
    You will select from ROCK, PAPER, or SCISSORS.
    The CPU will select ROCK, PAPER, or SCISSORS at random.
      
    1) ROCK BEATS SCISSORS 
    2) SCISSORS BEATS PAPER 
    3) PAPER BEATS ROCK
    """)
    # Does another part of this program eed to access this information?
    # IF YES, YOU MUST HAVE A return STATEMENT 
    # IF N0, A return STATEMENT IS NOT REQUIRED 

def playerChoice():
    playerChoice = input("Please enter rock,paper, or scissors and press enter.\n").lower()
    if  playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
        if  playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print( "You are not following directions. PLease try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    return playerChoice

def cpuChoice():
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
    return cpuChoice

# MAIN GAME LOOP
while playerscore < 5 and cpuScore < 5:
    print(f"{playerName}you have {playerscore}points.\nThe CPU has {cpuScore}points.\n")
   

# let cpu select choice at random.

if playerChoice=="rock" and cpuChoice == "paper":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The Cpu wins a point.\n")
        cpuScore +=1
elif playerChoice == "rock" and cpuChoice ==" scissors":
        # PLAYER WINS
        print(f" The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerscore +=1
elif playerChoice == "rock" and cpuChoice == "rock":
        # Draw
        print(f"The CPU chose {cpuChoice}and you chose {playerChoice}.\n")
        print("It's a draw!\n")
elif playerChoice == "scissors" and cpuChoice == "rock":
        # CPU WINS  
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
elif playerChoice == "scissors" and cpuChoice == "paper":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice}and you chose {playerChoice}.\n")
        print("you win a point.\n")
        playerscore += 1
elif playerChoice == "scissors" and cpuChoice == "scissors":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}. \n")
        print("It's a draw! \n")
elif playerChoice =="paper" and cpuChoice == "rock":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice}and you chose {playerChoice}. \n")
        print("You win a point. \n")
        playerscore += 1
elif playerChoice == "paper" and cpuChoice == "paper":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}. \n")
        print ("It's a draw! \n")
elif playerChoice == "paper" and cpuChoice == "scissors" :
        # CPU WINS
        print (f"The CPU chose {cpuChoice}and you chose {playerChoice}. \n")
        print ("The CPU wins a point. \n" )
        cpuScore += 1
else:
        print ("Unable to determine a winner. Please restart. \n")
        exit()


print(f"Your Final Score: {playerscore}CPU Final Score: {cpuScore}\n")
if playerscore > cpuScore:
        print (f"Congratulations {playerName}, a winner is you! \n")
elif cpuScore > playerscore:
        print (f"CPU wins. You are a disappointment to all. \n")
else:
        print("Unable to determine a winner. (nPlease restart. \n")
        exit()