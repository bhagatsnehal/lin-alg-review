"""
Problem: reshape-matrix
Difficulty: Easy
Link: https://www.deep-ml.com/problems/3?from=Linear%20Algebra
"""

import numpy as np

def reshape_matrix_scratch(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

	h, w = len(a), len(a[0])

	if h*w != new_shape[0]*new_shape[1]:
		return []

	flattened_matrix = [ele for row in a for ele in row]

	new_h, new_w = new_shape
	# new_w is the stride length
	reshaped_matrix = [flattened_matrix[i*new_w: (i+1)*new_w] for i in range(new_h)]

	return reshaped_matrix
	

def reshape_matrix_numpy(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Return a python list after reshaping by using numpy's tolist() method

	h, w = len(a), len(a[0])

	if h*w != new_shape[0]*new_shape[1]:
		return []

	reshaped_matrix = np.array(a).reshape(new_shape)

	return reshaped_matrix.tolist()


# What numpy stores for any array:

# A flat buffer of raw data in memory — never changes on reshape
# Shape — how many elements along each dimension e.g. (2, 3)
# Strides — how many bytes to jump in memory to move one step along each dimension

# So for a (2, 3) float64 array stored row-major:
    # data:    [1, 2, 3, 4, 5, 6]
    # shape:   (2, 3)
    # strides: (24, 8)   # 24 bytes to jump a row, 8 bytes to jump a column
# Reshape to (3, 2):
    # data:    [1, 2, 3, 4, 5, 6]  # identical, untouched
    # shape:   (3, 2)
    # strides: (16, 8)   # just recomputed
# Reshape is O(1) — only the metadata changes, not the data.