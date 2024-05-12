from turtle import Turtle
## Constants
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

MOVE_DISTANCE = 20

UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] ## The first segment of the snake

    ## this method creates a new snake instance
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        ## Add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
         # for loop moves the last segment to the position of the preceding 
        # This code essentially makes the snake segments move in the same direction as the first segment
        for seg_number in range(len(self.segments)-1, 0, -1):
            ## getting the position fo the penultimate segment
            new_x=self.segments[seg_number -1].xcor()
            new_y=self.segments[seg_number -1].ycor()

            ## move the last segment to the position of the penultimate segment 
            self.segments[seg_number].goto(new_x, new_y)

        # To move the first segment forward by 20 paces
        self.head.forward(MOVE_DISTANCE)

    ## methods created to control the snake headings UP DOWN LEFT RIGHT
    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    
