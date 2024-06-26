from turtle import Turtle
import random

COLOR = ["red", "orange", "green", "blue", "purple", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.all_cars = []
    
    def create_car(self):
        random_chance = random.randint(1,10)

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLOR))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    