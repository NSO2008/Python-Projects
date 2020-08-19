#turtle is a GUI used for drawing
import turtle
#turtle.color('yellow')
#turtle.forward(100)
#turtle.color('green')
#turtle.right(90)
#turtle.color('red')
#turtle.forward(100)
#turtle.right(90)
#turtle.color('blue')
#turtle.forward(100)
#turtle.color('orange')
#turtle.right(90)
#turtle.color('pink')
#turtle.forward(100)

#The 'range' keyword signifies how many times the loop is to run
for steps in range(10):
    turtle.color('purple')
    turtle.forward(100)
    turtle.right(360/10)
    turtle.forward(100)
    turtle.right(360/10)
    for more in range(10):
        turtle.color('purple')
        turtle.forward(75)
        turtle.right(360/10)
        turtle.forward(75)
        turtle.right(360/10)
        for morenmore in range(10):
            turtle.color('purple')
            turtle.forward(50)
            turtle.right(360/10)
            turtle.forward(50)
            turtle.right(360/10)
            for evenmore in range(10):
                turtle.color('purple')
                turtle.forward(25)
                turtle.right(360/10)
                turtle.forward(25)
                turtle.right(360/10)

turtle.done()