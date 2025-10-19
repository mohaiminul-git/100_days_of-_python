import turtle as t
import numpy as np

import random
tim=t.Turtle()
view= t.Screen()
t.colormode(255)
tim.pensize(10)
tim.speed(10)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b
    


rand_num=np.arange(1, 101)
#print(rand_num)
direction=["left","right"]

for _ in range(100):
    rand_dir=random.choice(direction)
    r,g,b=random_color()
    tim.pencolor((r, g, b))
    if rand_dir =="left":
        tim.left(90)
        #tim.forward(random.choice(rand_num))
        tim.forward(50)
    else:
        tim.right(90)
        #tim.forward(random.choice(rand_num))
        tim.forward(50)
        

