from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scorebaord = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    ## Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh() ## change the position of the food
        snake.extend() ## extends the length of the snake
        scorebaord.increase_score() ## increase the score on scoreboard

    ## Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scorebaord.game_over()

    ## Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scorebaord.game_over()
        
        




screen.exitonclick()