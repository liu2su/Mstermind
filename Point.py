'''
This file contains a class Point with two attributes, x and y.
It represents a geometric point with x and y coordinates. It has two methods:
delta_x, which takes as input another Point, and returns the absolute distance
of the different between this point and the other point's x coordinates,
delta_y, which takes an input another Point, and returns the absolute value
of the difference between this point and the other point's y coordinates.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)
