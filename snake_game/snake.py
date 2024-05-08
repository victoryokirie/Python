from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    ## this method creates a new snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

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
        self.segments[0].forward(MOVE_DISTANCE)

