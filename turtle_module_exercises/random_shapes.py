import turtle as t 
import random

timmy = t.Turtle()
timmy.shape("turtle")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy.goto(0,50)



### Random shapes
def draw_shape(sides):
    angle = 360/sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side in range (3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side)

    

screen = t.Screen()
screen.exitonclick()