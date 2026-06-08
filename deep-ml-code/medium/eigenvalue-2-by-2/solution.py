"""
Problem: eigenvalues-2-by-2
Difficulty: Medium
Link: https://www.deep-ml.com/problems/6
"""

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	mean = (matrix[0][0] + matrix[1][1]) / 2
	determinant = matrix[0][0] * matrix[1][1] - matrix[0][1]* matrix[1][0]

	eigenvalues = []

	assert mean**2 - determinant >= 0, "Complex eigenvalues not supported"

	# m +/- sqrt(m**2 - p) -- ting!

	eigenvalues.append(mean + (mean**2 - determinant)**0.5)
	eigenvalues.append(mean - (mean**2 - determinant)**0.5)

	return eigenvalues