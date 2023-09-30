import logging
from utility import Utility
from puzzle import Puzzle

class App:

    def __init__(self):  
        self._util = Utility()
        self._util.ConfigureLogging()

    def Process(self):
        try:
            logging.info('*** Start ***')
            
            puzzle = Puzzle()
            puzzle.Process()

            logging.info('*** Stop ***')
        except BaseException as ex:
            logging.exception(ex)

app = App()
app.Process()