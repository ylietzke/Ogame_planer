import abc
import json

# Übungsdatei Python 2
name1 = "Yannick "
age1 = "(24) "
name_age1 = name1 + age1
name2 = "Max "
age2 = "(25) "
name_age2 = name2 + age2
strings = name_age1 + "and " + name_age2 + "are strings!"
print (strings)

Story = name_age1 + "and " + name_age2 + "are starting with Python on Visual Studio Codes."
print (Story)

password = input ("Enter your password: ") #raw_input wird hier durch input ersetzt.
story2 = "Your password is: " + password
print (story2)

capital = "This text will be written just in big letters and consisted 71 letters."
print (len(capital))
print (capital.upper())

small = "This text consists just small letters."
print (small.lower())


# Kapitel "Go with the Flow"
def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take  or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
      print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
      print ("Of course this is the Argument Room, I've told you that already!")
    else:
      print ("You didn't pick left or right! Try again.")
      clinic()

clinic()

# importiert alle in dem math - Module enthaltenen Funktionen
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print (everything) # Prints 'em all!

# Kapitel "The Big If"
# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print (grade_converter(92))

# This should print a "C"
print (grade_converter(70))

# This should print an "F"
print (grade_converter(61))

#weitere Tests:

print ("Welcome to another test!")

variable1 = input ("Enter a word: ")

if  len(variable1) > 0 and len(variable1) < 6:
    
    print ("Dieses Passwort geht okay!")

else:
    print ("Dieses Passwort ist nicht ok!")

# What good are functions? Noch nicht funktionstüchtig!
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print ("With tax: %f") % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print ("With tip: %f") % bill
    return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
