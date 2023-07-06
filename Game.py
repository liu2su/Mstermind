from Marble import *
from Peg import *
from Point import *
import random
from ErrorLog import *
import time
'''
This file is a big class of the whole game
'''

class Game:
    def __init__(self,username,user_color = [], marble = [], peg = [], bottom = [], code = [], score = 0, column = 0, row = 0,\
                 peg_column = 0, peg_row = 0, mouse_x = -110, mouse_y = 275, user_data =[]):
        ''' 
        1.username:player's username                         2.user_color: a list to store the code user guesses
        3.marble: a list to store marble on the game board   4.peg: a list to store marble on the game board 5
        5.bottom:a list to store marble on the game board    6.code: secret color 
        7.score:user's score                                 8.column and row: index of marble 
        9.peg_column and peg_row: index of peg               10.mouse_x and mouse_y: cordinate of an arrow showing which line the player is typing
        11.user_data: data read from leaderboard.txt
        '''
        self.username = username
        self.user_color = user_color
        self.bottom = bottom
        self.marble = marble
        self.peg = peg
        self.code = self.generate_color()
        self.score = score
        self.column = column
        self.row = row
        self.peg_column = peg_column
        self.peg_row = peg_row
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.user_data = user_data
    def creat_marble(self):
        '''
        Creat marbles of gameboard as instances of class Marble and store them into attribute self.marble
        '''
        try:
            marble_line = []
            default_x = -300
            default_y = 260
            for i in range(0, 10):
                default_x = -300
                marble_line = []
                for j in range(0, 4):
                    up_marble = Marble(Point(default_x,default_y), "white")
                    marble_line.append(up_marble)
                    default_x =default_x + 50
                default_y =default_y - 40
                self.marble.append(marble_line)
        except ValueError or TypeError or IndexError as error:
            error1 = ErrorLog(error)
            error1.error_log()

    def creat_peg(self):
        '''
        Creat pegs of gameboard as instances of class Peg and store them into attribute self.peg
        '''
        peg_line = []
        y1 = 280
        for a in range(0, 10):
            peg_line = []
            for i in range(0, 2):
                x1 = -50
                for j in range(0, 2):
                    pegs = Peg(Point(x1, y1), "white")
                    peg_line.append(pegs)
                    x1 = x1 + 20
                y1 = y1 - 12
            y1 = y1 - 16
            self.peg.append(peg_line)

    def creat_bottom(self):
        '''
        Creat marbles of dashboard as instances of class Marble store them into attribute self.bottom
        '''
        bottom_marble1 = Marble(Point(-325, -240), "red")
        self.bottom.append(bottom_marble1)
        bottom_marble2 = Marble(Point(-275, -240), "blue")
        self.bottom.append(bottom_marble2)
        bottom_marble3 = Marble(Point(-225, -240), "green")
        self.bottom.append(bottom_marble3)
        bottom_marble4 = Marble(Point(-175, -240), "yellow")
        self.bottom.append(bottom_marble4)
        bottom_marble5 = Marble(Point(-125, -240), "purple")
        self.bottom.append(bottom_marble5)
        bottom_marble6 = Marble(Point(-75, -240), "black")
        self.bottom.append(bottom_marble6)
        
    def draw_marble(self):
        '''
        print marble to the game board
        '''
        for i in range(0, 10):
            for j in range(0, 4):
                self.marble[i][j].draw_empty()

    def draw_peg(self):
        '''
        print peg to the game board
        '''
        for i in range(0, 10):
            for j in range(0, 4):
                self.peg[i][j].draw_empty()

    def draw_bottom(self):
        '''
        print marble to the dashboard
        '''
        for i in range(0, 6):
            self.bottom[i].draw()

    def generate_color(self):
        '''
        Generate secret colors and store them into attribute self.code.
        '''
        try:
            colors = ['red', 'blue', 'green', 'yellow', 'purple', 'black']
            color_code = {1:'red', 2:'blue', 3:'green', 4:'yellow', 5:'purple', 6:'black'}
            secret_code = []
            secret_code_key = random.sample(range(1, 7), 4)
            for i in range(len(secret_code_key)):
                secret_code.append(color_code[secret_code_key[i]])
            return secret_code

        except ValueError or TypeError or IndexError as error:
            error1 = ErrorLog(error)
            error1.error_log()

    def leader_board(self):
        '''
        This method includs three parts:
        try block: Try to find and open leaderboard.txt, if the doesn't exist. Call except block.
        
        except block: Execute when the file does not exist, creat a new file, pop up a image and
        log the error.
        
        finally block: Execute after finding or creating leaderboard.txt:
                1.read the data line by line from leaderboard.txt.
                2.make a subset of each username and the score corresponding to the username.
                3.conbime all the subset into one set: self.user_data.
                4.sort the set, prin out top 10 elemenst to the leaderboard by using for loop.
        '''
        try:
            turtle.penup()
            turtle.goto(100, 270)
            turtle.pendown()
            turtle.write('Leaders:', font=("Verdana", 15, "normal"))
            user_file = open('leaderboard.txt', 'r')
            # read data from leaderboard.txt and store the data line by line into self.user_data
            user_file.close()    
                
        except FileNotFoundError as error:
            new_file = open('leaderboard.txt', 'w') 
            screen = turtle.Screen()
            screen.addshape('leaderboard_error.gif')
            turtle.shape('leaderboard_error.gif')
            turtle.penup()
            turtle.goto(205, 200)
            turtle.stamp()
            turtle.goto(100, 100)
            turtle.write('New file has been \nautomatically created',font=("Verdana", 10, "normal"))
            error1 = ErrorLog(error)
            error1.error_log()
            
        finally:
            user_file = open('leaderboard.txt', 'r')
            user_data_list = []
            user_data_index = 0
            for line in user_file:
                user_data_list.append(line.strip())
            length = int(len(user_data_list)) // 2
            for i in range(length):
                user_data_sub_list = []
                for j in range(0,2):
                    if user_data_index % 2 == 0:
                        user_data_list[user_data_index] = int(user_data_list[user_data_index])
                    user_data_sub_list.append(user_data_list[user_data_index])
                    user_data_index = user_data_index + 1
                self.user_data.append(user_data_sub_list)                
            self.user_data = sorted(self.user_data)
            data_x = 100
            data_y = 230
            # Print user_name and score to the screen
            if len(self.user_data) <=10:
                for i in range(length):
                    for j in range(1, -1, -1):
                        turtle.penup()
                        turtle.goto(data_x, data_y)
                        turtle.pendown() 
                        turtle.write(self.user_data[i][j], font=("Verdana", 15, "normal"))
                        data_x = data_x + 210
                    data_x = 100
                    data_y = data_y - 30
            else:
                for i in range(0,10):
                    for j in range(1, -1, -1):
                        turtle.penup()
                        turtle.goto(data_x, data_y)
                        turtle.pendown() 
                        turtle.write(self.user_data[i][j], font=("Verdana", 15, "normal"))
                        data_x = data_x + 210
                    data_x = 100
                    data_y = data_y - 30
                
            user_file.close()
            
    def click(self, click_x, click_y):
        '''
        The click() method is called when user clicking on the dashboard to determine which button the user is clicking.
        '''
        try:
            '''
            Check if the user click the quit button.
            If is True, print gif, wait 4 seconds and quit
            '''
            if click_x < 290 and click_x > 190 and click_y < -210 and click_y > -270:
                screen = turtle.Screen()
                screen.addshape('quitmsg.gif')
                turtle.penup()
                turtle.goto(0, 0)
                turtle.pendown()
                turtle.shape('quitmsg.gif')
                time.sleep(3)
                exit()
                
            '''
            Check if the user click the xbutton.
            If is True, reset the marble on the dashboard and reset
            the line of Marbles on the game board which the user is typing
            '''
            if click_x < 130 and click_x > 70 and click_y < -210 and click_y > -270:
                self.user_color.clear()
                for i in range(6):
                    self.bottom[i].draw()
                for j in range(4):
                    self.marble[self.row][j].draw_empty()
                self.column = 0
                
            '''
            Check if the user click the check_button
            Check if win:
                If win, print out win.gif, record user_name and score. Quit game
                If not win, reset bottom marble, column = column + 1. Clear user_color，score + 1
            It won't work if you click checkbutton but the len(user_color) !=4
            Move the triangle to indicate the number of lines.
            If column == 10 which means the player runs out of chance of guessing, print 'Lose.gif' and quit
            '''
            if click_x < 45 and click_x > -15 and click_y < -210 and click_y > -270 and len(self.user_color) == 4:
                self.score = self.score + 1
                for i in range(len(self.code)):
                    if self.user_color[i] in self.code:
                        self.peg[self.peg_row][self.peg_column].set_color('red')
                        self.peg[self.peg_row][self.peg_column].draw()
                        self.peg_column = self.peg_column + 1
                self.peg_column = 0
                
                for i in range(len(self.code)):
                    if self.user_color[i] == self.code[i]:
                        self.peg[self.peg_row][self.peg_column].set_color('black')
                        self.peg[self.peg_row][self.peg_column].draw()
                        self.peg_column = self.peg_column + 1
                self.peg_column = 0
                if self.peg[self.peg_row][3].get_color() == 'black':
                    screen = turtle.Screen()
                    screen.addshape('winner.gif')
                    turtle.penup()
                    turtle.goto(0,0)
                    turtle.pendown()
                    turtle.shape('winner.gif')
                    input_userdata = []
                    input_userdata.append(self.score)
                    input_userdata.append(self.username)
                    self.user_data.append(input_userdata)
                    self.user_data = sorted(self.user_data)
                    length = int(len(self.user_data))
                    user_file = open('leaderboard.txt', 'w')
                    for i in range(length):
                        for j in range(0, 2):
                            user_file.write(str(self.user_data[i][j]))
                            user_file.write('\n')
                    user_file.close()
                    time.sleep(2)
                    exit()
                if self.row != 9:
                    self.peg_row = self.peg_row + 1
                    self.mouse_y = self.mouse_y - 40
                    turtle.penup()
                    turtle.goto(self.mouse_x, self.mouse_y)
                    turtle.pendown()        
                                           
                self.user_color.clear()
                for i in range(6):
                    self.bottom[i].draw()
                self.row = self.row + 1
                self.column = 0
                '''
                if self. == 10, which means the user has run out of chance, print Lose.gif and quit
                '''
                if self.row == 10:
                    screen = turtle.Screen()
                    screen.addshape('Lose.gif')
                    turtle.penup()
                    turtle.goto(0, 0)
                    turtle.pendown()
                    turtle.shape('Lose.gif')
                    time.sleep(4)
                    exit()
            '''
            The six if statements below are associaed with six insances of Class Marble.
            Once user click marbles on dashboard, call method is_empty() to check if the marble has been clicked,
            if it is not.the system will get the color of the marble which user clicked and use set_color()
            to print color to the marble which user is guessing.
            '''
            if self.bottom[0].clicked_in_region(click_x,click_y) == True and self.bottom[0].is_empty == False and len(self.user_color) != 4:
                self.user_color.append(self.bottom[0].get_color())
                self.bottom[0].draw_empty()
                self.marble[self.row][self.column].set_color(self.bottom[0].get_color())
                self.marble[self.row][self.column].draw()
                self.column = self.column + 1
            if self.bottom[1].clicked_in_region(click_x,click_y) == True and self.bottom[1].is_empty == False and len(self.user_color) != 4:
                self.user_color.append(self.bottom[1].get_color())
                self.bottom[1].draw_empty()
                self.marble[self.row][self.column].set_color(self.bottom[1].get_color())
                self.marble[self.row][self.column].draw()
                self.column = self.column + 1
            if self.bottom[2].clicked_in_region(click_x,click_y) == True and self.bottom[2].is_empty == False and len(self.user_color) != 4:
                self.user_color.append(self.bottom[2].get_color())
                self.bottom[2].draw_empty()
                self.marble[self.row][self.column].set_color(self.bottom[2].get_color())
                self.marble[self.row][self.column].draw()
                self.column = self.column + 1  
            if self.bottom[3].clicked_in_region(click_x,click_y) == True and self.bottom[3].is_empty == False and len(self.user_color) != 4:
                self.user_color.append(self.bottom[3].get_color())
                self.bottom[3].draw_empty()
                self.marble[self.row][self.column].set_color(self.bottom[3].get_color())
                self.marble[self.row][self.column].draw()
                self.column = self.column + 1
            if self.bottom[4].clicked_in_region(click_x,click_y) == True and self.bottom[4].is_empty == False and len(self.user_color) != 4:
                self.user_color.append(self.bottom[4].get_color())
                self.bottom[4].draw_empty()
                self.marble[self.row][self.column].set_color(self.bottom[4].get_color())
                self.marble[self.row][self.column].draw()
                self.column = self.column + 1    
            if self.bottom[5].clicked_in_region(click_x,click_y) == True and self.bottom[5].is_empty == False and len(self.user_color) != 4:
                self.user_color.append(self.bottom[5].get_color())
                self.bottom[5].draw_empty()
                self.marble[self.row][self.column].set_color(self.bottom[5].get_color())
                self.marble[self.row][self.column].draw()
                self.column = self.column + 1
        except IndexError or TypeError or SyntaxError  as error:
            error1 = ErrorLog(error)
            error1.error_log()

def main():
    '''
    A quick test function, ignore it :)  
    '''
    test = Game('user')
    code = test.code
    print(test.username)

if __name__ == '__main__':
    main()
                
    
