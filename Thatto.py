import turtle
from turtle import *

a=turtle.Screen()
b=turtle.Turtle()

b.shape("turtle")
b.color("red")
a.bgcolor("black")
b.penup()
b.left(543)
b.fd(270)
b.right(93)
b.fd(200)
b.pensize(8)
b.bk(50)

#Letra "T"
b.pendown()
b.bk(100)
b.fd(100)
b.left(90)
b.fd(50)
b.bk(100)
b.penup()
b.bk(70)
b.left(90)

#Letra "H"
b.pendown()
b.fd(100)
b.bk(50)
b.left(90)
b.fd(50)
b.left(90)
b.fd(50)
b.bk(100)
b.right(90)
b.penup()
b.fd(70)
b.left(65)

#Letra "A"
b.pendown()
b.fd(110)
b.right(130)
b.fd(110)
b.bk(43)
b.right(115)
b.fd(50)
b.right(90)
b.penup()
b.fd(60)
b.right(90)
b.fd(110)

#Letra "T"
b.pendown()
b.fd(50)
b.right(90)
b.fd(100)
b.bk(100)
b.left(90)
b.fd(50)
b.penup()
b.fd(70)

#Letra "T"
b.pendown()
b.fd(50)
b.right(90)
b.fd(100)
b.bk(100)
b.left(90)
b.fd(50)
b.penup()
b.fd(80)

#Letra "O"
b.begin_fill()
b.pendown()
b.circle(-50,355)


b.penup()
b.right(90)
b.fd(45)
b.end_fill()
b.penup()
done()