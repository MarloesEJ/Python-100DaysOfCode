# import colorgram
# colors = colorgram.extract('hirstdotspainting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     listOfColors.append((r, g, b))

import turtle
from random import randint

listOfColors = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48),
                (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63),
                (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43),
                (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95),
                (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2),
                (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172),
                (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]

turtle.colormode(255)

theTurtle = turtle.Turtle()
theTurtle.hideturtle()
theTurtle.penup()
theTurtle.speed(6)


y_cor = -250
x_cor = -250

dotSize = 20
distanceBetweenDots = 50


def get_random_color():
    return randint(0, len(listOfColors) - 1)


for i in range(10):
    theTurtle.goto(x_cor, y_cor)
    for j in range(10):
        if j == 9:
            y_cor += 50
        theTurtle.dot(dotSize, listOfColors[get_random_color()])
        theTurtle.forward(distanceBetweenDots)


screen = turtle.Screen()
screen.exitonclick()
