"""
Problem: mean-by-row-or-column
Difficulty: Easy
Link: https://www.deep-ml.com/problems/4?from=Linear%20Algebra
"""

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
    """
	Python function that calculates the mean of a matrix either by row or by column, based on a given mode.
    The function should take a matrix (list of lists) and a mode ('row' or 'column') as input 
	and return a list of means according to the specified mode.
	"""

    if mode == "column":
        means = [sum(block)/len(block) for block in zip(*matrix)]
    else:
        means = [sum(row)/len(row) for row in matrix]
    return means