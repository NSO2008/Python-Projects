import turtle
color = input("This is a fun etch n' sketch program, perfect for the kids! \nEnter the color of your pen to begin: ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

while color.lower() not in colors:
    color = input("I am sorry but that color is not supported... Supported colors include: \nRed\nOrange\nYellow\nGreen\nBlue\nPurple...\nSo which color have you chosen?: ")


length = int(input("Now enter a number from 1 to 100(No decimal points)as your length(in pixels): "))

lengthOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

while length not in lengthOptions:
    length = int(input("Sorry but your input is invalid...\nTry again: "))

angle = int(input("Please enter the number of sides of your shape(1-100): "))

angleOptions = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

while length not in angleOptions:
    angle = int(input("Sorry, but your have inputted an invalid answer...\nTry again: "))


fill = input("And what color would you like the shape filled in?: ")

fillColors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

while fill.lower() not in fillColors:
    fill = input("I am sorry but that color is not supported... Supported colors include: \nRed\nOrange\nYellow\nGreen\nBlue\nPurple...\nSo which color have you chosen?: ")


bgcolor = input("And finally, enter your background color: ")

bgcolors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

while bgcolor.lower() not in bgcolors:
    bgcolor = input("I am sorry but that color is not supported... Supported colors include: \nRed\nOrange\nYellow\nGreen\nBlue\nPurple...\nSo which color have you chosen?")


print("Image window opened... ")


turtle.title("Etch N' Sketch!")

turtle.bgcolor(bgcolor)

turtle.color(color)

turtle.fillcolor(fill)

turtle.begin_fill()
for steps in range(angle):
    turtle.forward(length)
    turtle.right(360/angle)
turtle.end_fill()

turtle.done()

print("Window closed.")