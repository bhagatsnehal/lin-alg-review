"""
Problem: mean-by-row-or-column
Difficulty: Easy
Link: https://www.deep-ml.com/problems/4?from=Linear%20Algebra
"""

import torch

def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:
    """
    Calculate mean of a 2D matrix per row or per column using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of means or raises ValueError on invalid mode.
    """
    a_t = torch.as_tensor(matrix, dtype=torch.float)
    # Your implementation here
    if mode == "column":
        axs = 0
    else:
        axs = 1

    return a_t.mean(axis = axs)
