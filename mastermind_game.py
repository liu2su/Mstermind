import turtle
from Marble import *
from Peg import *
from Point import *
from Game import *
from add_shape import *
from ErrorLog import *
from draw_the_board import draw_the_board

'''
mastermind_game.py is used to call the functions
and methods from other files,including draw the marble,
draw the screen,add image and so on.
'''

    
def main():
    x = -110
    y = 275
    turtle.title('Mastermind by Liu2su')
    user_name = turtle.textinput('CS 5001 by Liu2su', 'Your name:')#cheat code:)
    if user_name == None:
        exit()
    else:
        game = Game(user_name)
        draw_the_board()
        game.creat_marble()
        game.creat_peg()
        game.creat_bottom()
        add_shape()
        game.draw_marble()
        game.draw_peg()
        game.draw_bottom()
        game.leader_board()
        if user_name == 'liu2su':
            print(game.code)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.shape('triangle')
        turtle.right(180)
        turtle.st()
        turtle.onscreenclick(game.click)
        

if __name__ == '__main__':
    main()
