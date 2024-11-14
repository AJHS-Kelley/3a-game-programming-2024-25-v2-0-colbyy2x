# # Functions Practice, Jacolby Allen, v0.0

# import random

# def helloWorldMulti(): # FUNCTION SIGNATURE
#     """ This function will output Hello, World! in a language the user choose.""" # DOCSTRING \
#     # print a list of languages to the screen, at least three but no more than five.
#     print("The avaliable languages are English, Spanish, French")
    
#     # allow the user to select (input) a choice for the language.
#     lanaguage = input("What langauge do you want?")
    
#     # print " Hello, World!" to the screeb in that lanaguage 
#     if lanaguage == "English":
#         print("In English:\nHello, World!\n")
#     elif lanaguage == " Spanish":
#         print("In Spanish:\nHola, Mundo!\n")
#     elif lanaguage == "French":
#         print("In French:\nBon jour, Le Monde!\n")
#     else:
#         print("In Somali: \n, Haye caalamkow!\n")

# helloWorldMulti()

# # Function tp Detetmine Even / Odd Numbers 
# argument1 = random.randint(-1000, 1000)

# def isEven(argument: int) -> bool:
#     """Determines is an integer value is even or odd."""
#     if argument % 2 ==0:
#         return True
#     else:
#         return False 
# isEven()

# print(isEven(argument1))

# # Function with Multiple Arguments
# def canRideRollerCoaster(age:int, height: int) -> bool:
#     if age > 10 and height > 4:
#         print("You can ride.\n")
#         return True
#     else:
#         print("You cannot ride.\n")
#         return False
    

def canGraduate(numCredits: int, GPA:float) -> bool:
    if numCredits > 23 and GPA > 2.0:
        return True
    elif numCredits > 20 and GPA > 3.0:
        return True
    else:
        return False