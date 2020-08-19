#The input keyword is used to collect user input...
#While any keyword on the LHS is used for storing variables...
#Variables can't contain spaces...
name = input("Write your name right here: ")
name = name.capitalize()
try:
    print("Hey " + name)
except NameError:
    print("There is an error with my variable assignment... \nYou know what? Let's forget it...")
finally:
    print("Moving on...")
my_name = "Bryan"
print(my_name + " is my name...")
name_two = input("What's your Last name? Write it here: ")
name_two = name_two.capitalize()
try:
    print("You're pretty smart " + name + " " + name_two + "...")
except NameError:
    print("There is something wrong with my code... \nYou know what... let's forget it...")
finally:
    print("Bye for now...")