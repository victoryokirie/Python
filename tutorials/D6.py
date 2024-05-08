#while loops: this loop will continue running while a condition is true. it only stops when a condition becomes false
# while somethine_is_true:
#   do something repeatedly

#For Loop use: when you want to iterate over something and you want to do something with each thing that you are iterating over

#while loop use: when you dont really care what number in a sequence you in, which item you are iterating through in a list and you just simply want to carry out some sort of functionality as long as a condition is true, then use while loops

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move