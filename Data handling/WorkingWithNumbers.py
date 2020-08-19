#You do not put quotes around a number unless it is in a piece of text...
#To turn a number in string form into an integer... 
#Make use of the int() function...
#To do vice versa the str() function is used...
#There are different symbols of operation... 
#But take notice of the "%" symbol and the "**" symbol
#The "%" symbol shows you what would be the remainder if you divided a number...
#It is called "Modulo"
#The "**" symbol is equivalent to the phrase; "raised to the power of"...
#It is called "Exponentiation"
area = 0
height = input("Please insert the height:")
base = input("Please insert the base width: ")

#Convert all values to floating numbers(Keep in mind a user can type any value including decimals)...
try:
    height = float(height)
except ValueError:
    print("Hey... are you sure you put actual numbers up there? \nNow I'm giving you another chance... if you mess it up, my code will jumble up and you'll probably receive some mumbo jumbo error")
    height = input("Now insert the correct height: ")
    height = float(height)
    
try:
    base = float(base)
except ValueError:
    print("Hey... are you sure you put actual numbers up there? \nNow I'm giving you another chance... if you mess it up, my code will jumble up and you'll probably receive some mumbo jumbo error")
    base = input("Now insert the correct base width: ")
    base = float(base)

#This is code programmed to calculate the area of a triangle...
area = height * base /2

#Finally... print the result...
try:
    print("The area of the triangle is " + str(area))
except ValueError:
    print("Hey... are you sure you put actual numbers up there? \n If you didn't, to bad, I can't really go back to that line...")
finally:
    print("There, you have your result, hopefully you are satisfied, and now the code can end.")

