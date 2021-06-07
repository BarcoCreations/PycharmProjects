from turtle import Turtle, Screen
import random
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

tim = Turtle()


# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
colors = ["alice blue", "dodger blue", "green yellow", "dark orange", "goldenrod", "cyan", "red	", "saddle brown"]


def move(geometric):
    angle = 360 / geometric
    for turn in range(geometric):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    move(shape_side_n)

