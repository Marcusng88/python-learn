# dots drawing with random color
# 10x10 drawing
from turtle import Turtle,Screen
import random
import turtle
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg',20)
the_turtle = Turtle()
the_turtle.shape("arrow")
turtle.colormode(255)
for i in colors:
   r = i.rgb.r
   g = i.rgb.g
   b = i.rgb.b
   
   rgb_colors.append((r,g,b))

row =-200
the_turtle.teleport(-200,-200)
the_turtle.speed('fastest')
for i in range(10):
    for j in range(10):
        the_turtle.pendown()
        the_turtle.color(random.choice(rgb_colors))
        the_turtle.dot(20)
        the_turtle.penup()
        the_turtle.forward(50)
    row += 50  
    the_turtle.teleport(x=-200, y=row) 

    

      
      
screen = Screen()
screen.exitonclick()
