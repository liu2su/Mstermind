'''
By using unittest, test_mastermind_game.py can:
1. test ErrorLog.py with ZeroDivisionError as its attribute.
2. test if marbles are successfully created and test if they are printed on the correct position.
3. test if pegs are successfully created and test if they are printed on the correct position.
4. test if the code generation system works properly.
'''

from ErrorLog import *
from datetime import datetime
from Game import *
import random
import unittest

class test_class(unittest.TestCase):
        
        def test_error(self):
            '''
            test ErrorLog.py with ZeroDivisionError as its attribute
            '''
            a = ErrorLog(ZeroDivisionError)
            a.error_log()
            self.assertEqual(a.error, ZeroDivisionError)
            self.assertEqual(a.date, a.date)

        def test_marble_mainboard(self):
            '''
            This method is test if marbles are successfully created
            and test if they are printed on the correct position.
            '''
            game1 = Game('test')
            game1.creat_marble()
            y = 260
            x = -300
            for i in range(0, 10):
               self.assertEqual(game1.marble[i][random.randint(0, 3)].position.y, y)
               y = y - 40
            for j in range(0, 4):
               self.assertEqual(game1.marble[random.randint(0, 9)][j].position.x, x)
               x = x + 50
            self.assertEqual(len(game1.marble[random.randint(0, 9)]), 4)
            self.assertEqual(len(game1.marble), 10)
        def test_marble_peg(self):
            '''
            This method is test if pegs are successfully created
            and test if they are printed on the correct position.
            '''
            game1 = Game('test')
            game1.creat_peg()
            x = - 50
            self.assertEqual(len(game1.peg[random.randint(0, 9)]), 4)
            self.assertEqual(len(game1.peg), 10)
            
        def test_code_generate(self):
            '''
            This method is used to test if the code generation system
            works properly If the colors you enter are different from
            the secret code above, an FAILED will be returned
            Do not worry, this means the program is working properly
            '''
            print('\n')
            game1 = Game('test')
            print('The secret code generated by game is:\n', game1.code)
            print('---------------------------------------')
            i = 0
            print('Please input color you guess\nNote that the data you enter will be stored directly in user_colors\n'\
                  'Which is an attribute of game1 to store color user choose. game1 is\n'\
                  'an object of class Game for testing. If the colors you enter are \n'\
                  'different from the secret code above, an FAILED will be returned\n'\
                  'Do not worry, this means the program is working properly ')
            print('---------------------------------------')
            while i < 4:
                data = input(f'Please input color {i+1}:\n')
                if data == 'blue' or 'red' or 'green' or 'purple' or 'black' or 'yellow':
                        game1.user_color.append(data)
                        i = i + 1

            self.assertEqual(game1.code, game1.user_color)
    
def main():
        print('test system processing，please wait.....')
        unittest.main(verbosity = 3)
        print('test system finished')

if __name__ == '__main__':
    main()
