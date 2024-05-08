from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
is_race_on = False
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()