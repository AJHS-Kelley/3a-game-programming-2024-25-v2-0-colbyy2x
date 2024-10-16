# ROCK,PAPER, SCISSORS by Jacolby Allen, v0.0

# MODULE IMPORTS 
import random, time

# DATA STRUCTURES -- PLAYER
playerscore = 0
playerChoice= None
numDraws=0

#DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
loopCount= 0 
loopsReq = int(input("How many loops do you want?\nEnter an integer, no commas, and press ENTER.\n"))
rpsTimeStart = time.time() 
while loopCount < loopsReq:
        # let cpu select choice at random.
    cpuChoice= random.randint(0,2) # randomly select 0,1, or 2
    if cpuChoice == 0:
        cpuChoice="rock"
    elif cpuChoice == 1:
        cpuChoice == "scissors"        
    elif cpuChoice == 2:
         cpuChoice == "paper"
    else:
        print("Unable to determine CPU choice.\nPlease restart. \n")
        exit()
    playerChoice= random.randint(0,2) # randomly select 0,1, or 2
    if playerChoice ==0:
        playerChoice="rock"
    elif playerChoice == 1:
        playerChoice == "scissors"        
    elif playerChoice == 2:
        playerChoice == "paper"
    
    else:
        print("Unable to determine CPU choice.\nPlease restart. \n")
        exit()
    
    # compare player choice to cpu choice
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
        numDraws += 1
    elif playerChoice == "paper" and cpuChoice == "scissors" :
       # CPU WINS
        print (f"The CPU chose {cpuChoice}and you chose {playerChoice}. \n")
        print ("The CPU wins a point. \n" )
        cpuScore += 1
    else :
        print("unable to determine a winner. Please restart.\n")
        exit()
    loopCount +=1 

print(f"Your Final Score: {playerscore}\nCpu Final Score: {cpuScore}\nDraws: {numDraws}\n")
if playerscore > cpuScore:
    print(f"Congratulations the player wins.\n")
elif cpuScore > playerscore:
    print(f"The CPU wins. You are a dissapoinment to all.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()

rpsTimeStop= time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of loops: {loopCount}\n")
print(f"Execution Time: {rpsTime: .2F} seconds\n") 