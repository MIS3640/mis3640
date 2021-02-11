import turtle
from turtle_shape import arc, circle, move, polygon


def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


def main():
    t = turtle.Turtle()
    t.speed(0)
    flower(t, 6, 60.0, 60.0)

    move(t, 0, -60)
    circle(t, 60)

    t.hideturtle()
    turtle.Screen().mainloop()


if __name__ == '__main__':
    main()
