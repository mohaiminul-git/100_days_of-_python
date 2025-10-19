
from turtle import Turtle, Screen
import random

is_game_on = False


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_tourtles = []
y = -178
for col in colors:

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(col)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 70
    all_tourtles.append(new_turtle)
    
if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_tourtles:
        if turtle.xcor() > 210:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is the winner!")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner!")
            
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    
    
    


screen.exitonclick()

# t = Turtle()
# screen = Screen()

# def forward():
#     t.forward(10)

# def backword():
#     t.backward(10)

# def counter_clock():
#     t.left(10)
    
# def clock_wise():
#     t.right(10)

# screen.listen()             # start listening for events
# screen.onkey(fun=forward, key="w")
# screen.onkey(fun=backword, key="s")
# screen.onkey(fun=counter_clock, key="a")
# screen.onkey(fun=clock_wise, key="d")

# screen.mainloop()           # keep window open and responsive
