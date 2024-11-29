# Data Types and Operators, JaColby Allen, v0.7

# Fundamental Data Types
# String - str- sequence of letters, numbers, spaces, or other characters.
# Strings in python are unsude '' or " "

# Boolean - bool - True of False values. 

# Float - float- any number value with a decimal, +/- including 0.

# Integers - int - any whole number, +/-, including 0.

# Data types ate stored in VARIABLES.
# A variable is basically a bucket with a namd to put data into.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CANNOT START WITH A NUMBER.
# camelCaseVariableNames
# snake_case_variable_names

# DECLEARING VARIABLES AND ASSIGNING VALUES 

high_score = 7662 #int data type

car_speed = 1.55 # float data type, miles per hour

hasAxe = True # boolean data type
isyellow = False # boolean data type 

playerName = "Jacolby Allen" # string data type 
enemyName = "Kennedy spencer" # string data type

# ASSIGN NEW VALUES 
playerName = "Jacolby Allen" #string data type
car_speed = 1.55

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAx = 5.0

# Printing Data Types
newInt = 3
newFloat = 4.0
newString = "Long Live Foolio"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))

#printing Variables to Console / Screen
# print(high_score)
# print(car_speed)
# print(playerName)
# print(isyellow)
# print(enemyName)

# printing variables and expressions to console / screen 
# print(high_score + 25000)
# print(9 * 13)
# print(enemyName)


# PRINTING VARIABLES INSIDE OF STRINGS
# print(f"Hello {playerName}") 

# ARITHMETIC OPERATORS 
myInt = 5
myFloat = 7.9
myNum = 4

# Addition 
myInt = 5 + 13
myFloat = 7.9 + 16.3

myInt = myInt + 7

myNum = myInt + myFloat
# When you add an int and a float together, the answer becomes a float.

# subtraction 
myNum = myInt - myFloat
myInt = myFloat - 1.50

# Division 
myNum = myInt * myFloat # fist is numerator, second num is denominator.

# Modulus (Modulo)%-- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MODULUS IS DETEMINING EVEN/ NUMBERS.
numStudents = 9
numSlicesPizza = 81

leftOvers = numSlicesPizza % numStudents

# Exponents **
numSquared = 5**2 % 5 is BaseException

# Floor division // -- Divides, the throws out and decimal.
# myNum = myInt // myFloat

# Addition- Assignmet Operators - Mostly used for counters.
myNum = 4
myNum = myNum + 1 # Old-Schooled Mehtod 
myNum +=1 #NEW HOTNESS 
myNum *=1
myNum /=1


# COMPARISON OPERATORS
# IS-EQUAL-TO -- Are the two valuesequal to each other?
# Returns True or False based on evaluation.
x = 12.0
print(x == 5)

# NOT-EQUAL-TO != Are the two values NOT equal?
# Returns True or False based on evaluation.
print(x !=12)

# GREATER THAN / GREATER-THAN-OR-EQUAL TO
print(5 > 3) # Greater Than
print(12 >= 2) # Greater Than or Equal To

# LESS THAN / LESS-THAN-OR-EQUAL TO
print(5 < 3) # LESS Than
print(12 <= 2) # LESS Than or Equal To

# LOGICAL OPERATORS 
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATMENT TO BE TRUE
age = 22
height = 80.5
eyeColor = "Cyan"
# In order to ride the Teacups, you must be at least 18 years or older and at least 60" tall.
print(age >=18 and height >= 60)
print(age >=18 and height >= 60 and eyeColor == "Red")
# ALWAYS CHECK FOR THE LEAST-LIKELY TO BE FALSE CONDITION FIRST!!!
# print(defeatedBoss == True and level > 5 and hasBlueKey == True)

# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
print(age >=18 and height >= 60)
print(age >=18 and height >= 60 and eyeColor == "Red")
# ALWAYS CHECK FOR THE LEAST-LIKELY TO BE TRUE CONDITION FIRST!!!
# print(defeatedBoss == True and level > 5 and hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT 
a = 5
print(a == 5)
print(not (not(a ==5)))

# # COMBINING LOGICAL OPERATORS 
print("a =8 and hasKey = True or isCloud")
# TRUE and

# IDENITY OPERATORS
g = 1.0
h = 1.0
i = g 
print( g is h)
print(i is h)
print(i is not 1.0)
print( i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)


