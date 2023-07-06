from datetime import datetime
class ErrorLog():
    '''
    When an error occurs in the game, this file will be called to generate
    an instance of ErrorLog including the date and error type as attributes.
    The date and type of error will write into mastermind_errors.err.txt
    '''
    def __init__(self,error,date = datetime.now()):
        '''
        Take date and error type as attributes
        '''
        self.error = error
        self.date = date

    def error_log(self):
        '''
        Write date and type of error into mastermind_errors.err.txt
        '''
        error_file = open('mastermind_errors.err.txt','a')
        log_text = 'Exception date time:' + str(self.date) + '\nError: '+ str(self.error) + '\n'
        error_file.write(log_text)
        error_file.close()
