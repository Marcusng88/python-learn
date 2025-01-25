# turtle race

# uses random steps
from turtle import Turtle ,Screen
import random

screen = Screen()
screen.setup(width=400,height=400)
user_bet =screen.textinput(title='Make your bet',prompt='Which turtle will win the race ? Enter a color:')
list = ['one','two','three','four','five','six','seven']
colors = ['red','orange','yellow','green','blue','violet','purple']
turtle_list =[]
start_y = -80
for x,i in enumerate(list):
    i = Turtle(shape='turtle')
    i.penup()
    i.color(colors[x])
    i.goto(x=-200,y=start_y)
    turtle_list.append(i)
    start_y+=20



def move(turtle):
    turtle.forward(random.randint(0,10))

def check(turtle):
    return turtle.xcor()>=170

while True:
    checks = False
    for x,i in enumerate(turtle_list):
        if check(i):
            winner = colors[x]
            checks =True
            
    if (checks==True):
        break
    move(turtle_list[0])
    move(turtle_list[1])
    move(turtle_list[2])
    move(turtle_list[3])
    move(turtle_list[4])
    move(turtle_list[5])
    move(turtle_list[6])




if winner==user_bet:
    print('You win')
else:
    print (f'You lose , the winner is {winner}')


screen.exitonclick()