import turtle
from ErrorLog import *
'''
print image (for example: quit.gif) to the scrren.
'''
def add_shape():
    try:
        #add quit.gif to the dashboard
        screen = turtle.Screen()
        screen.addshape('quit.gif')
        turtle.shape('quit.gif')
        turtle.penup()
        turtle.goto(240, -240)
        turtle.pendown()
        turtle.stamp()
        #add quit.gif to the dashboard
        screen.addshape("xbutton.gif")
        turtle.shape('xbutton.gif')
        turtle.penup()
        turtle.goto(100, -240)
        turtle.pendown()
        turtle.stamp()
        #add checkbutton.gif to the dashboard
        screen.addshape("checkbutton.gif")
        turtle.shape('checkbutton.gif')
        turtle.penup()
        turtle.goto(15, -240)
        turtle.pendown()
        turtle.stamp()
        #add logo to the dashboard
        screen.addshape("logo.gif")
        turtle.shape('logo.gif')
        turtle.penup()
        turtle.goto(-160, -125)
        turtle.pendown()
        turtle.stamp()
    except AttributeError or FileNotFoundError as error:
        error1 = ErrorLog(error)
        error1.error_log()

