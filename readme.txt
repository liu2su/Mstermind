Hint: Having hard time guessing color? Input my Github name which is 'liu2su' as your username. The secret code will print on IDLE ：）
The screen of the game is divided into three parts:
1.game board to show marbles ang pegs
2.dashboard to allow user to choose, check,reset colors and quit
3.leaderboard to show top 10 of players

Part I: Game.py
It is the most important file of this game. The Game is a big class of the whole game, includes: 
I.attributes: 
    1.username:player's username                                     2.user_color: a list to store the code user guesses
    3.marble: a list to store marble on the game board    4.peg: a list to store marble on the game board 5
    5.bottom:a list to store marble on the game board    6.code: secret color 
    7.score:user's score                                                      8.column and row: index of marble 
    9.peg_column and peg_row: index of peg                   9.mouse_x and mouse_y: cordinate of an arrow showing which line the player is typing
    11.user_data: data read from leaderboard.txt
II.methods
#creat_marble(self):
    Creat marbles of gameboard as instances of class Marble and store them into attribute self.marble
#creat_peg(self):
    Creat pegs of gameboard as instances of class Peg and store them into attribute self.peg
#creat_bottom(self):
    Creat marbles of dashboard as instances of class Marble store them into attribute self.bottom
#three method to draw mable and peg on the screen
#generate_color(self):
    Generate secret colors and store them into attribute self.code.
#leader_board(self):
    This method includs three parts:
        (1)try block: Try to find and open leaderboard.txt, if the doesn't exist. Call except block.    
        (2)except block: Execute when the file does not exist, creat a new file, pop up a image and log the error.     
        (3)finally block: Execute after finding or creating leaderboard.txt:
                1.read the data line by line from leaderboard.txt.
                2.make a subset of each username and the score corresponding to the username.
                3.conbime all the subset into one set: self.user_data.
                4.sort the set, prin out top 10 elemenst to the leaderboard by using for loop.
#click(self, click_x, click_y):
    The click() method is called when user clicking on the dashboard to determine which button the user is clicking.
        (1)If the user is clicking the 'checkbutton' :
            1.Check if win:
                If win, print out win.gif, record user_name and score. Quit game
	If not win, reset bottom marbles, column = column + 1. Clear user_color，score + 1
            2. It won't work if you click checkbutton but the len(user_color) !=4
            3. Move the triangle to indicate the number of lines.
            4. If column == 10 which means the player runs out of chance of guessing, print 'Lose.gif' andquit
        (2)If the user is clicking the 'quit' button:	
            1.Print out 'quit.gif' and quit
        (1)If the user is clicking the marble:
            1.Once user click marbles on dashboard, call method is_empty() to check if the marble has been clicked,
                If return False, the system will get the color of the marble which user clicked and use set_color() to print color to the marble which user is guessing.
                If return True, nothing happen.
        
Part II: mastermind_game.py
    The job of mastermind_game.py is to call the functions and methods from other files, including draw the marble, draw the screen,add image and so on, 
    mastermind_game.py is just like an airport where various planes(functions and methods) take off or land at the airport.
Part III: ErrorLog.py:
    When an error occurs in the game, this file will be called to generate an instance of ErrorLog including the date and error type as attributes.
    The date and type of error will write into mastermind_errors.err.txt
Part IV: test_mastermind_game.py
    By using unittest, test_mastermind_game.py can:
        1. test ErrorLog.py with ZeroDivisionError as its attribute.
        2. test if marbles are successfully created and test if they are printed on the correct position.
        3. test if pegs are successfully created and test if they are printed on the correct position.
        4. test if the code generation system works properly.
Part V: other files
    #add_shape.py: print image (for example: quit.gif) to the scrren.
    #draw_the_board.py: draw the game board, leader board and dashboard
    #Peg.py: This file contains a class Peg with the attributes pen, color, position, visible, is_empty, and size. This class can draw an empty peg and set its color, 
                   get its color, erase itself, and determine if it has been clicked. This class requires the use of the class Point.
    #Marble.py: This file contains a class Marble with the attributes pen, color, position, visible, is_empty, and size. This class can draw an empty Marble and 
                         set its color, get its color, erase itself, and determine if it has been clicked. This class requires the use of the class Point.
    #Point.py: This file contains a class Point with two attributes, x and y. It represents a geometric point with x and y coordinates. It has two methods:
                     delta_x, which takes as input another Point, and returns the absolute distance of the different between this point and the other point's x coordinates,
                     delta_y, which takes an input another Point, and returns the absolute value of the difference between this point and the other point's y coordinates.
 THAT'S ALL, HAVE FUN!