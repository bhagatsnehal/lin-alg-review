"""
Problem: matrix-vector-dot-product
Difficulty: Easy
Link: https://www.deep-ml.com/problems/1?from=Linear+Algebra
"""


import torch

def matrix_dot_vector(a, b) -> torch.Tensor:
    """
    Compute the product of matrix `a` and vector `b` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of length m, or tensor(-1) if dimensions mismatch.
    """
    a_t = torch.as_tensor(a, dtype=torch.float)
    b_t = torch.as_tensor(b, dtype=torch.float)
    # print(a_t)
    # Dimension mismatch check
    h, w = a_t.shape

    if w != b_t.size(0):
        return torch.tensor(-1)

    return a_t @ b_t
