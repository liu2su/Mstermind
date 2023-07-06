'''
This file contains a class Marble with the attributes pen, color,
position, visible, is_empty, and size. This class can draw an
empty Marble and set its color, get its color, erase itself, and
determine if it has been clicked. This class requires the use of the class Point.
'''
import turtle
from Point import Point

MARBLE_RADIUS = 15

class Marble:
    def __init__(self, position, color, size = MARBLE_RADIUS):
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
        if abs(x - self.position.x) <= 20  and \
           abs(y - self.position.y) <= 20 :
            return True
        return False


def main():
    marble = Marble(Point(200,200), "blue")
    marble.draw_empty()
    k = input("enter something here and I'll fill the marble > ")
    marble.draw_empty()
    k = input("enter something here and I'll erase the marble > ")
    marble.erase()

if __name__ == "__main__":
    main()
