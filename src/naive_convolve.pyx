import numpy as np

cimport numpy as cnp
cimport cython


@cython.boundscheck(False)
@cython.wraparound(False)
def naive_convolve(cnp.ndarray grid, int N):
    cdef cnp.ndarray[cnp.int_t, ndim=2] copy
    cdef int i, j
    cdef int lengthx, lengthy
    cdef int temp

    copy = np.empty((N, N), dtype=int)
    lengthx = len(grid[0]) - 1
    for i in range(1, lengthx):
        for j in range(1, lengthx):
            temp = np.sum(grid[i-1:i+2, j-1:j+2].flatten())
            if grid[i, j] == 1:
                if temp > 4 or temp < 3:
                    copy[i, j] = 0
            elif grid[i, j] == 0:
                if temp == 4:
                    copy[i, j] = 1
    return copy
