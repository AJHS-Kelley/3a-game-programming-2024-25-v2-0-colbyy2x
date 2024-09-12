# Awarding Extra Lives, Jacolby Allen, V0.0

lives = 2
score =  int (input("Please type an INTERGER number and press enter.\n"))
name = "bolby"
# print(f"Hello { name} YOu scored a 10000.\n")

# Allow the user input the score AS AN INTERGER.

# If score is 1000 or less 
    # Lose a Life
# If score is . 10000 but less that 1000001
    # Give 1 Extra Life
# If score is > 100000
    # Give 2 Extra Lives 

# Output the score and number of lives to the screen.
# BEGIN CODE HERE

if score <=10000:
    print(" Player has lost an life.\n")
    lives = -1
    print(f"Hello { name} YOu scored {score} Thanks for playing.\n")

elif score >= 10001:
    print("Player Has Gained An Extra Life.\n")
    lives += 1
    print(f"Hello { name} YOu scored {score} Thanks for playing.\n")

elif score> 100000:
    lives += 2
    print("Player has gained 2 extra lives.\n")

    print(f"Hello { name} YOu scored {score} Thanks for playing.\n")

