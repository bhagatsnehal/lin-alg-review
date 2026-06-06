"""
Problem: matrix-times-matrix
Difficulty: Medium
Link: https://www.deep-ml.com/problems/9?from=Linear+Algebra
"""

import numpy as np

def matrixmul_scratch(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    
    if len(a[0]) != len(b):
        return -1

    c = []
    for row in a:
        current_row = []
        for col in zip(*b):
            current_row.append(sum([x*y for x,y in zip(row, col)]))
        c.append(current_row)

    return c


def matrixmul_numpy(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    
    if len(a[0]) != len(b):
        return -1

    c = np.array(a) @ np.array(b)

    return c