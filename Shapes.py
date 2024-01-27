import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(10)
        tim.right(angle)


for shape in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape)

screen = Screen()
screen.exitonclick()