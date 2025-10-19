import turtle as t


timmy = t.Turtle()

timmy.shape("turtle")

timmy.color("red")


for _ in range(4):
    
    timmy.forward(100)
    
    timmy.right(90)
    


from turtle import Screen
view=Screen()
view.exitonclick()