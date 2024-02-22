import turtle

theTurtle = turtle.Turtle()
screen = turtle.Screen()
screen.listen()


def move_forward():
    theTurtle.forward(10)


def move_backward():
    theTurtle.backward(10)


def turn_left():
    theTurtle.left(10)


def turn_right():
    theTurtle.right(10)


def clear_screen():
    theTurtle.clear()
    theTurtle.penup()
    theTurtle.home()
    theTurtle.pendown()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
