from turtle import *
color('red', 'lightgreen')
begin_fill()
bgcolor("black")
pu()
# backward(300)
pd()
while True:
    forward(450)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
left(90)
pensize(5)
circle(-205,360)
done()