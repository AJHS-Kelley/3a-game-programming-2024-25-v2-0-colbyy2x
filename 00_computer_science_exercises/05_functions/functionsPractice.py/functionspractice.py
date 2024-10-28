# Functions Practice, Jacolby Allen, v0.0

import random

def helloWorldMulti(): # FUNCTION SIGNATURE
    """ This function will output Hello, World! in a language the user choose.""" # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five.
    print("The avaliable languages are English, Spanish, French")
    
    # allow the user to select (input) a choice for the language.
    lanaguage = input("What langauge do you want?")
    
    # print " Hello, World!" to the screeb in that lanaguage 
    if language == "English":
        print("In English:\nHello, World!\n")
    elif langauge == " Spanish":
        print("In Spanish:\nHola, Mundo!\n")
    elif language == "French":
        print("In French:\nBon jour, Le Monde!\n")
    else:
        print("In Somali: \n, Haye caalamkow!\n")

helloWorldMulti() # FUNCTION CALL

# Function tp Detetmine Even / Odd Numbers 
argument1 = random.randint(-1000, 1000)

def isEven(argument: int) -> bool # Requires one ARGUMENT (argument1) and RETURNS a Boolean value.
    """Determines is an integer value is even or odd."""
    if argument % 2 ==0:
        return True
    else:
        return False 
isEven()
