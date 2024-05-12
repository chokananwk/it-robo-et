from turtle import *

t = Turtle()
t.speed(10)
t.pensize(4)

def vshave():
    t.left(25)
    t.forward(25)
    t.left(180)
    t.forward(25)
    t.left(130)
    t.forward(25)
    t.left(180)
    t.forward(25)
    t.left(205)
    
def bran():
    t.forward(25)
    vshave()
    t.forward(25)
    vshave()
    t.forward(25)
    vshave()
    t.forward(25)
    vshave()
    t.left(180)
    t.forward(100)
    
def main():
    for i in range(0,4):
        t.left(60)
        bran()
        bran()

mainloop()