# User Input Practice, JaColby Allen, v0.0

# input() is the built-in function to get information from the KEYBOARD.
# BASIC EXAMPLE
variableName = input("Please type a variable name and press enter.\n")
print(variableName)

# Input() saves ALL IINPUT TO STRING DATA TYPES BY DEFAULT!!!
# Input() saves ALL IINPUT TO STRING DATA TYPES BY DEFAULT!!!
# Input() saves ALL IINPUT TO STRING DATA TYPES BY DEFAULT!!!
# Input() saves ALL IINPUT TO STRING DATA TYPES BY DEFAULT!!!

# INCORRECT, CAUSE A CONCATENATION ERROR.
# myNumber = input(" Please type an INTERGER number and press enter.\n")
# print(myNumber + 5)

# CORRECT --Use a wrapper.
myNumber = int (input("Please type an INTERGER number and press enter.\n"))
print(myNumber + 5)

# Wrapper Functions
#int() will convert the data to an INTERGER if possible.
newNumber = input("Please type a value and press enter.\n")
print(int(newNumber)) # can convert STRING to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert INTEGER to STRING.

#float() will convert the data to a FLOAT if possible.
newNumber = input(" Please type a value and press enter.\n")
#print(int(newNumber)) <-- cannot convert FLOAT to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert FLOAT to STRING.

# str() will convert the data to a STRING if possible.
newNumber = 5 
print( newNumber + newNumber) # Should print 10
print(str( newNumber + newNumber))# Should print 55.
