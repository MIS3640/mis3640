import turtle
from turtle_shape import arc, circle, move, polygon


def draw_yinyang(t):
    # large circle
    circle(t, 100)

    # two arcs
    move(t, 0, 100)
    t.setheading(180)
    arc(t, 50, 180)

    move(t, 0, 100)
    t.setheading(0)
    arc(t, 50, 180)

    # small circles
    move(t, 0, 50 + 100 / 6)
    circle(t, 100 / 6)

    move(t, 0, 150 + 100 / 6)
    circle(t, 100 / 6)


def main():
    t = turtle.Turtle()
    t.speed(0)

    draw_yinyang(t)
    turtle.Screen().mainloop()


if __name__ == '__main__':
    main()
