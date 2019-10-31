import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

matrix_1 = np.array(np.loadtxt(fname="matrix_1.txt"))
matrix_2 = np.array(np.loadtxt(fname="matrix_2.txt"))

distance, path = fastdtw(matrix_1, matrix_2, dist=euclidean)

print(distance)