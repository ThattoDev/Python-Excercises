from turtle import *
color('red', 'yellow')
begin_fill()
bgcolor("black")
penup()
# backward(300)
pendown()
while True:
    forward(400)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
left(90)
pensize(5)
circle(-205,360)
done()