*Implementing Conways Game of Life*.

Naive implementation in Python.
-Uses a randomly generated ndarray as the starting point.
-In order to generate the next grid, app makes a call to naive_convolve, a cython function that takes in the current grid, creates an equal sized zeroed array and then naively populates it using the rules of Conways Game of Life, after which it returns the new array. Uses cython because pure python was too slow.
TODO: A visualization of the grids, viewing the grids in terminal doesnt work very well.

