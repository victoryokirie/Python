from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    # for loop moves the last segment to the position of the preceding 
    # This code essentially makes the snake segments move in the same direction as the first segment
    for seg_number in range(len(segments)-1, 0, -1):
        new_x=segments[seg_number -1].xcor()
        new_y=segments[seg_number -1].ycor()

        segments[seg_number].goto(new_x, new_y)

    # To move the first segment forward by 20 paces
    segments[0].forward(20)

        
        















screen.exitonclick()