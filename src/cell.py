import numpy 
from p5 import *

'''
what is life?

    Environment, E
        --the number of neighbours required to prevent a currently living cell from expiring

    Fertility, F 
        --the number of neighbours required to create a new living cell

    Transition rule, R
        --the 4 tuple (El,Eu,Fl,Fu)

    
    Conways Game of life
        --Transition rule, R =  (2333)
        --Environment rules would be
            --no less than two living neighbours and no more than three living neighbours to remain alive, otherwise cell dies  
        --Fertility rules would be
            --exactly three living neighbours are required for a dead cell to come alive


Class Cell:
    The values that a cell would have access to
        Its own state, whether alive or dead
    Functions of a cell
        Cell outputs a pixel on the screen.
        Cell changes colour of this pixel


Class Grid:
numpyarray
    -receives a rule.
    -receives an initial configuration
    -mutating an array forward in generations, called by next would be convenient

'''







class Cell:

    #reflect values on table.
    #if value is one, cell is alive/red
    #if value is zero, cell is dead/blue
    #they know nothing about their neighbours
    #must be called to change, do not maintain constant access to table

    def __init__(self, position):
        self.position = position
        self._state = False #false is dead, 

    def __repr__(self):
        return f"Cell at X:{self.position[0]}, Y:{self.position[1]}, currently {'alive' if self._state else 'dead'}"
        
    @property
    def state(self):
        return self._state

    def kill(self):
        self._state = False

    def create(self):
        self._state = True