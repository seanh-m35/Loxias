from .database import cldbconfig
from pathlib import Path
from .readfiles import *

class main(object):
    """
    main class allows access to the rest of the package
    """
    def __init__(self):
        pass

    def readfiles(self):
        """
        Used to load data files into the database
        """
        x = clprocessfiles()

    def runtychebot(self):
        """
        Runs the bot
        """

if __name__ == "__main__":
    x = main()
