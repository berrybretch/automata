import time
from p5 import *
import pickle
from grid import Grid
from time import sleep
import numpy as np

grid = Grid(length=20)
def setup():
	size(604,604)
	title("testing grounds")


def draw():
	background(50)
	grid._next()
	stroke(0)
	fill(255,0,0)
	for array in grid.series:
		with np.nditer(array, flags=['multi_index']) as itr:
			for item in itr:
				if item == 1:
					circle((itr.multi_index[0]*(604/22), itr.multi_index[1]*(604/22)), 30)
	
if __name__ == "__main__":
	run()
