"""
Problem: vector-projection-on-line
Difficulty: Easy
Link: https://www.deep-ml.com/problems/66
"""


def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	# L^T (v - Lx)
	# x = L^Tv/L^TL
	# p = Lx

	L_norm_sq = sum(a**2 for a in L)
	dot_product = sum(a*b for a, b in zip(v, L))

	projection_vector = [a*(dot_product/L_norm_sq) for a in L]

	return projection_vector
