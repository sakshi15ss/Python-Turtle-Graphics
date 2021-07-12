import turtle
import time
import random
t=turtle.Turtle()
s=turtle.Screen()
t.hideturtle()
s.title("SKY")
s.screensize(800,500,bg="black")
t.pencolor("white")
#t.speed(1)
def star():
    for i in range(5):
        t.pendown()
        t.forward(10)
        # time.sleep(2)
        t.right(144)
      
while True:
    x=random.randint(-400,250)
    y=random.randint(-400,250)
    t.penup()
    t.goto(x,y)
    star()


turtle.done()