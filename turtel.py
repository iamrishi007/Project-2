import turtle
t=turtle.Turtle()
paint=["purple","red","blue","orange","yellow","green"]

for i in range(200):
    t.color(paint[i%6])
    t.pensize(i/7+1)
    t.forward(i)
    t.left(70)