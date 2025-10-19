from turtle import Turtle,Screen

tim=Turtle()
tim.pensize(1)
view=Screen()
#tim.setposition(0,0)

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

view.exitonclick()