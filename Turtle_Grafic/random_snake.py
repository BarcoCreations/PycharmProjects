import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
#colors = ["alice blue", "dodger blue", "green yellow", "dark orange", "goldenrod", "cyan", "red", "saddle brown"]


direction = [0, 90, 180, 270, 360]
tim.pensize(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def move():
    tim.setheading(random.choice(direction))
    tim.forward(40)

print(random_color())
for shape_side_n in range(1, 100):
    tim.color(random_color())
    move()