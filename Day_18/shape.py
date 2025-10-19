import turtle as t

import random
tim=t.Turtle()
view= t.Screen()


num_side=[4,5,6,7,8,9,10]

colour=[]
for i in num_side:
    for _ in range(i):
        tim.color(random.choice(color))
        tim.forward(50)
        tim.right(360/i)
        
view.exitonclick()