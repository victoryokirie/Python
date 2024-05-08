import turtle as t 
import random

timmy = t.Turtle()
timmy.shape("turtle")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed(10)




for movement in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))







screen = t.Screen()
screen.exitonclick()
