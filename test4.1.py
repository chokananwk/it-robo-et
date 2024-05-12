from turtle import *

t = Turtle()
t.speed(10)
t.pensize(4)

for i in range(0,4):
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
mainloop()