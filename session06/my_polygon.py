import turtle
import math

leo = turtle.Turtle()
print(leo)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# leo.fd(100)
# leo.lt(90)

# for i in range(4):
#     leo.fd(100)
#     leo.lt(90)

# Exercise 2.1
def square(t):
    """this function takes a parameter named t, which is a turtle. It should use the turtle to draw a square."""
    for i in range(4):
        t.fd(100)
        t.lt(90)


# square(leo)

# raphael = turtle.Turtle()
# square(raphael)

# Exercise 2.2


def square(t, length):
    """this function takes a parameter named t, which is a turtle, and another parameter length, which is a float. It should use the turtle to draw a square with side length, length."""
    for i in range(4):
        t.fd(length)
        t.lt(90)


# square(leo, 200)

# Exercise 2.3
def polygon(t, length, n):
    """draws an n-sided regular polygon"""
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


# polygon(t=leo, n=20, length=50)


# Exercise 2.4


def circle(t, r):
    """draws an approximate circle"""
    # import math
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


# circle(leo, 200)

# Exercise 2.5


def arc(t, r, angle):
    """draws an arc with angle"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


# arc(leo, 200, 90)
# arc(leo, 200, 360)

# the process of refactoring

def polyline(t, n, length, angle):
    """
    Draws n line segments with given length and angle (in degrees) between them.
    t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polyline(leo, n=4, length=100, angle=60)


def polygon(t, length, n):
    """
    Draws a n-sided polygon with given length. t is a turtle.
    """
    angle = 360 / n
    polyline(t, n, length, angle)

# polygon(leo, 200, 4)   

def arc(t, r, angle):
    """
    Draws an arc with radius r and angle. t is a turtle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)


def circle(t, r):
    """
    Draws a circle with radius r. t is a turtle.
    """
    arc(t, r, 360)
    

turtle.mainloop()