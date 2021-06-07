import random
import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
tim.up()
tim.hideturtle()
tim.setpos(-250, -250)


def one_row(row):
    for dot in range(1, 11):
        offset = dot * 50
        tim.dot(20, random.choice(color_list))
        if dot < 10:
            tim.setpos((-250 + offset), row)
        else:
            tim.left(90)
            tim.forward(50)
            tim.left(90)
            tim.forward(450)
            tim.left(180)


for column in range(0, 10):
    position = -250 + (column * 50)
    one_row(position)

my_screen = Screen()
my_screen.exitonclick()

