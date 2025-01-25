# etch a sketch app

# w to move forwards
# s to move backwards
# a to rotate counter clockwise
# d to rotate clockwise
# c to clear screen
from turtle import Turtle,Screen

screen =Screen()
the_turtle = Turtle()

def mov_forwards():
    the_turtle.forward(10)

def mov_backwards():
    the_turtle.backward(10)

def counter_clockwise():
    the_turtle.setheading(the_turtle.heading()-10)

def clockwise():
    the_turtle.setheading(the_turtle.heading()+10)

def clear():
    the_turtle.clear()
    the_turtle.teleport(0,0)

screen.listen()

def action():
    screen.onkey(key='w',fun=mov_forwards)
    screen.onkey(key='s',fun=mov_backwards)
    screen.onkey(key='a',fun=counter_clockwise)
    screen.onkey(key='d',fun=clockwise)
    screen.onkey(key='c',fun=clear)
        

action()

screen.exitonclick()