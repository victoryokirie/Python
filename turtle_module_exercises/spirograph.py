import turtle as t 
import random
t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r, g, b)
    return color

def draw_spirograph(gap_size):
    no_of_circles = int(360/gap_size)
    for _ in range(no_of_circles):
        timmy.color(random_color())
        timmy.circle(70)
        timmy.setheading(timmy.heading() + gap_size)


draw_spirograph(8)


















screen = t.Screen()
screen.exitonclick()
