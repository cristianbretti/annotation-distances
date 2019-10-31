import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw


matrix_1 = np.loadtxt(fname="matrix_1.txt")
matrix_2 = np.loadtxt(fname="matrix_2.txt")

x = np.array(matrix_1)
y = np.array(matrix_2)

distance, path = fastdtw(x, y, dist=euclidean)

print(distance)