from turtle import Screen, Turtle
import random
timmy = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]


def draw_shape(sides):
    angle = int(360 / sides)
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

for num_sides in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(num_sides)









screen = Screen()
screen.exitonclick()