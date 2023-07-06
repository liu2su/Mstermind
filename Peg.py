'''
This file contains a class Peg with the attributes pen, color, position,
visible, is_empty, and size. This class can draw an empty peg and set its color,
get its color, erase itself, and determine if it has been clicked. This class
requires the use of the class Point.
'''
import turtle
from Point import Point

PEG_RADIUS = 5

class Peg:
    def __init__(self, position, color, size = PEG_RADIUS):
        self.pen = self.new_pen()
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # set to fastest drawing

    def new_pen(self): 
        return turtle.Turtle()

    def set_color(self, color):
        self.color = color
        self.is_empty = False

    def get_color(self):
        return self.color

    def draw(self):
        # if self.visible and not self.is_empty:
            # return
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)
        
    def erase(self):
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x, y):
        if abs(x - self.position.x) <= self.size * 2 and \
           abs(y - self.position.y) <= self.size * 2:
            return True
        return False


def main():
    peg = Peg(Point(200,200), "red")
    peg.draw_empty()
    k = input("enter something here and I'll fill the peg > ")
    peg.draw()
    k = input("enter something here and I'll erase the peg > ")
    peg.erase()

if __name__ == "__main__":
    main()
