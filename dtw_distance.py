import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--first_id', type=int, default=1)
parser.add_argument('--second_id', type=int, default=2)

args = parser.parse_args()

first_id = args.first_id
second_id = args.second_id

matrix_1 = np.array(np.loadtxt(fname="matrix_%d.txt" %first_id))
matrix_2 = np.array(np.loadtxt(fname="matrix_%d.txt" %second_id))

distance, path = fastdtw(matrix_1, matrix_2, dist=euclidean)

print(distance)