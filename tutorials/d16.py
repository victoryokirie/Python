# from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# timmy.color("Red")

table = PrettyTable()
table.add_column("Pokemon_name", ["Victory", "Great", "Levi", "Ken"])
table.add_column("Type", ["Eagle", "Lion", "Panda", "Cheetah"])

print(table)
