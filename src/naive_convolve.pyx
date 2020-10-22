import numpy as np

cimport numpy as cnp
cimport cython


@cython.boundscheck(False)
@cython.wraparound(False)
def naive_convolve(cnp.ndarray grid, int N):
    cdef cnp.ndarray[cnp.int_t, ndim=2] new_array
    cdef int i, j
    cdef int lengthx
    cdef int temp

    new_array = np.zeros([N, N], dtype=np.int)
    for i in range(1, N-1):
        for j in range(1, N-1):
            temp = np.sum(grid[i-1:i+2 , j-1:j+2])
            if grid[i, j] == 1:
                if temp>4 or temp< 3:
                    new_array[i,j] = 0
            elif grid[i, j] == 0:
                if temp == 3:
                    new_array[i,j] = 1
    return new_array
    
    


