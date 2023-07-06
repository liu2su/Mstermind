'''
The screen of the game is divided into three parts:
1.game board to show marbles ang pegs
2.dashboard to allow user to choose, check,reset colors and quit
3.leaderboard to show top 10 of players

'''

import turtle

def draw_the_board():
    turtle.hideturtle()
    turtle.pensize(3)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-350,300)
    turtle.pendown()
    turtle.fd(400)
    turtle.right(90)
    turtle.fd(450)
    turtle.right(90)
    turtle.fd(400)
    turtle.right(90)
    turtle.fd(450)
    # the code above is used to draw mian borad.
    turtle.penup()
    turtle.goto(-350,-160)
    turtle.pendown()
    turtle.right(90)
    turtle.fd(700)
    turtle.right(90)
    turtle.fd(150)
    turtle.right(90)
    turtle.fd(700)
    turtle.right(90)
    turtle.fd(150)
    # the code above is used to draw dash borad.
    turtle.penup()
    turtle.goto(350,-150)
    turtle.pencolor('blue')
    turtle.pendown()
    turtle.fd(450)
    turtle.left(90)
    turtle.fd(290)
    turtle.left(90)
    turtle.fd(450)
    turtle.left(90)
    turtle.fd(290)
    # the code above is used to draw leader borad.
