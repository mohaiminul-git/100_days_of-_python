import colorgram
import random
import turtle as t
# colour=colorgram.extract("image.jpg",30)


# coloure_list=[]

# for i in colour:
#     rgb=i.rgb
#     r=rgb[0]
#     g=rgb[1]
#     b=rgb[2]
#     col=(r,g,b)
#     coloure_list.append(col)
    
# print(coloure_list)
list_of_colour=[(203, 165, 109), (150, 72, 48), (239, 245, 240), (232, 235, 241), (222, 202, 137), (171, 152, 41), (52, 93, 124), (135, 32, 23), (133, 162, 184), (198, 92, 72), (49, 123, 90), (14, 98, 74), (146, 178, 147), (69, 49, 41), (234, 176, 166), (162, 142, 157), (55, 45, 50), (150, 19, 23), (113, 75, 77), (185, 205, 174), (22, 82, 86), (48, 65, 81), (45, 61, 73), (90, 144, 126), (219, 177, 181), (108, 127, 154), (194, 83, 86), (178, 190, 208)]

tim=t.Turtle()
view= t.Screen()
t.colormode(255)
size = 225
gap = 50
dot_size = 20
tim.hideturtle()

for y in range(-size, size + 1, gap):
    for x in range(-size, size + 1, gap):
        tim.penup()
        
        tim.setposition(x,y)
       #tim.pendown()
        tim.dot(dot_size, random.choice(list_of_colour))


view.exitonclick()