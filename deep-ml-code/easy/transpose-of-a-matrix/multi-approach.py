"""
Problem: transpose-of-a-matrix
Difficulty: Easy
Link: https://www.deep-ml.com/problems/2?from=Linear%20Algebra
"""

import numpy as np
import torch

def transpose_matrix_scratch(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    
    h, w = len(a), len(a[0])

    out = []

    for j in range(w):
        new_row = []
        for i in range(h):
            new_row.append(a[i][j])     
        out.append(new_row)
    
    return out

    # list comprehension -  return [[a[i][j] for i in range(h)] for j in range(w)]
    # zip unpack -          return  [list(row) for row in zip(*a)]

def transpose_matrix_numpy(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """

    return np.array(a).T

def transpose_matrix_pytorch(a) -> torch.Tensor:
    """
    Transpose a 2D matrix `a` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a transposed tensor.
    """
    a_t = torch.as_tensor(a)
    
    return a_t.T

