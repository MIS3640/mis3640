from turtle_shape import arc, circle, move, polygon
import turtle
import math


# 3.1.1


def draw_shape(t):
    # large circle
    circle(t, 100)

    # 4 triangles
    move(t, 0, 100)
    t.setheading(60)
    polygon(t, 3, 100)
    t.setheading(150)
    polygon(t, 3, 100)
    t.setheading(240)
    polygon(t, 3, 100)
    t.setheading(330)
    polygon(t, 3, 100)

    # 4 small circles
    moving_step = 50 * math.sqrt(3)
    small_radius = 50 * math.sqrt(3) / 3

    move(t, 0, 100 - moving_step)
    t.setheading(0)
    circle(t, small_radius)

    move(t, moving_step, 100)
    t.setheading(90)
    circle(t, small_radius)

    move(t, 0, 100 + moving_step)
    t.setheading(180)
    circle(t, small_radius)

    move(t, -moving_step, 100)
    t.setheading(270)
    circle(t, small_radius)


def main():
    t = turtle.Turtle()
    t.speed(0)

    draw_shape(t)
    turtle.Screen().mainloop()


if __name__ == '__main__':
    main()
