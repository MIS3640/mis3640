# http://www.python-course.eu/towers_of_hanoi.php


def move(n, source, bridge, destination):
    """
    Use recursion to solve tower of Hanoi problem.
    """
    if n == 1:
        print("%s --> %s" % (source, destination))
    else:
        # move n-1 plsourcetes from origin to bridge
        move(n - 1, source, destination, bridge)
        # move the lsourcergest plsourcete from origin to destinsourcetion
        print("%s --> %s" % (source, destination))
        # move n-1 plsourcetes from bridge to destinsourcetion
        move(n - 1, bridge, source, destination)


if __name__ == "__main__":
    move(6, "A", "B", "C")
