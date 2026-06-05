"""
Problem: transpose-of-a-matrix
Difficulty: Easy
Link: https://www.deep-ml.com/problems/5?from=Linear%20Algebra
"""

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	
    """
    Python function that multiplies a matrix by a scalar and returns the result.
    """

    result = [[ele*scalar for ele in row] for row in matrix]
    return result


# EFFECT ON DETERMINANT

#  det⁡(cA)=c^n * det⁡(A) for an n×n matrix. 
#  Geometrically, each dimension/column vector is scaled by c - having a cumulative effect on the area.