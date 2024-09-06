# Flow Control structures, JaColby Allen, V.0
# Making Computer Programs Make Decisions

temperature = 200.80
color = "Green"
height = 10
likesPineappleOnPizza = True 

# SINGLE DECISION POINT - if Statement 
# if CONDITIONAL_EXPRESSION: <-- This will use COMPARISON OPERATOR 99% of the time.
  #runThisCode IF the CONDITIONAL_EXPRESSION is True       

if temperature > 90:
    print(" It is hot as the sun outside.\n")

if height > 9:
    print("You are not tall enough la bra.\n")

# CHEAT CODE FOR US STATEMENTS THAT USE BOOLEANS.
if likesPineappleOnPizza:
     print("That is very good")

# What if we wanted something different to happen?
if color =="Green": # COMMON ERROR FOR STUDENTS IS USING = instead of ==.
    print("Your shirt is the right color .\n")
else:
    print("Your shirt is not the correct color.\n")

if temperature > 100.80:
    print("Please go inside and cool off.\n")
else:
    print("You are good but please drink something.\n")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE 
# Must be > min. height and < max. height to ride.

if height >= 6:
    print("You are too tall enough to ride the roller coasters!\n")
elif height >= 3:
    print("You're tall to ride the roller coaster sorry!\n")
else: # " oh, no, somethings wrong!"
    print("Error, height not detected. Do not ride.\n")
    
# When writing if-e;if-else block check for the HIGHEST VALUE first using > or >=
if height >= 6:
    print("You are too tall enough to ride the roller coasters!\n")
elif height >= 3:
    print("You're tall to ride the roller coaster sorry!\n")
else: # " oh, no, somethings wrong!"
    print("Error, height not detected. Do not ride.\n")
 

 # When writing if-e;if-else block check for the LOWEST VALUE first using < or <=
if height <= 3:
    print("You not tall enough to ride the roller coasters!\n")
elif height < 6:
    print("You're tall enought to ride the roller coaster !\n")
else: # " oh, no, somethings wrong!"
    print("Error, height not detected. Do not ride.\n")

# Create an if-elif-else block that checks for temperature.
# If the temperature is at least 100, print thats its too hot outside.
# If the temperature is at least 50 degrees but less than 100, print that recess is allowed.
# If the temperature is at less than 50 degrees but greater than 0, print that recess is in the gym.
# If no temperature is detected, print an error message.

if temperature >= 100:
    print("It's too hot outside, students cannot go to recess.\n")
elif temperature >= 50:
    print("It's cool enough to go outside.\n")
elif temperature > 0:
    print("Recess will be in the gym.\n")
else:
    print("Error detcting temperature.\n")

