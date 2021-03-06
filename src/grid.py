from p5 import *
import numpy as np 
from naive_convolve import naive_convolve as naive 

class Grid:

    def __init__(self, length=1000):
        self.grid = np.random.choice([1,0], size=length*length).reshape(length, length)
        self.grid = np.pad(self.grid, pad_width=1)
        self.generation = 1
        self.series = [self.grid]

    def __repr__(self):
        return f'''Array_Shape <{self.grid.shape}>\nGeneration <{self.generation}>\n
        '''

    def _next(self):
        print(f"Building <{self.generation+1}>...")
        new = naive(self.grid, self.grid.shape[1])
        self.series.append(new)
        self.grid = new
        self.generation += 1
        print(f"Done building the generation <{self.generation}>")


