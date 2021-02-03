import math


r1 = 100
r2 = 2.5
r3 = 2021

# area1 = 3.14 * r1 * r1
# area2 = 3.14 * r2 * r2
# area3 = 3.14 * r3 * r3


def area_of_circle(radius):
    """return the area of a circle, given RADIUS which is a float"""
    # docstring
    area = math.pi * radius ** 2
    # print(area)
    return area


area1 = area_of_circle(1)
print(area1)

double_size = area1 * 2
print(double_size)


# area1 = area_of_circle(r1)
# area2 = area_of_circle(r2)
# area3 = area_of_circle(r3)

# print(area1, area2, area3)
