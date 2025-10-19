import turtle as t
import random
tim=t.Turtle()
view= t.Screen()
t.colormode(255)
t.speed(0)
t.pensize(3)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        current_pos=t.heading()
        r,g,b=random_color()
        t.pencolor(r,g,b)
        t.circle(150)
        t.setheading(current_pos+size_of_gap)
        
  
draw_spirograph(5)  
    
# for _ in range(500):
#     r,g,b=random_color()
#     t.pencolor(r,g,b)
#     t.circle(150)
#     t.left(10)
    
    
view.exitonclick()