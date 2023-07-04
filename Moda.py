import turtle
from turtle import *

turtle.Screen()
turtle.Turtle()

shape("turtle")
color('blue', 'lightgreen')
bgcolor("black")
penup()
left(180)
fd(300)
right(93)
pensize(8)


#Letra "M"
pd()
fd(100)
rt(145)
fd(60)
left(110)
fd(60)
rt(145)
fd(100)

#Space
pu()
lt(90)
fd(70)
pd()

#Letra "O"
circle(50,355)

#Space
pu()
lt(9)
fd(90)
pd()

#Letra "D"
lt(90)
fd(100)
rt(90)
circle(-50,175)

clearscreen()

turtle.screen.tracer(8, 25)
dist = 2
for i in range(200):
    fd(dist)
    rt(90)
    dist += 2

#Space
pu()
rt(185)
fd(100)
pd()

#Letra "A"


done()