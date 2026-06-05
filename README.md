# Linear Algebra Practice

Structured coding practice and study notes covering linear algebra fundamentals, worked through as part of a focused 2-day study sprint.

## Resources

| Resource | Link | Status |
|---|---|---|
| 3B1B — Essence of Linear Algebra | [YouTube Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | In Progress |
| MIT 18.06 — Gilbert Strang | [OCW Lectures](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/video_galleries/video-lectures/) | In Progress |
| Deep-ML — Linear Algebra Collection | [Problems](https://www.deep-ml.com/collections/Linear%20Algebra) | In Progress |

---

## Repo Structure

```
linear-algebra-practice/
│
├── README.md
│
├── deep_ml/
│   ├── easy/
│   │   ├── matrix_vector_product.py
│   │   ├── transpose.py
│   │   ├── reshape.py
│   │   ├── mean_by_row_col.py
│   │   ├── scalar_multiplication.py
│   │   ├── matrix_multiplication.py
│   │   └── matrix_transformation.py
│   ├── medium/
│   │   ├── covariance_matrix.py
│   │   ├── linear_regression_normal_eq.py
│   │   ├── determinant_4x4.py
│   │   ├── eigenvalues_2x2.py
│   │   └── matrix_inverse_2x2.py
│   └── hard/
│       ├── svd.py
│       ├── pca.py
│       └── qr_decomposition.py
│
└── notes/
    └── consolidation.md
```

---

## Problem Template

Each solution file follows this structure:

```python
"""
Problem: <Problem Name>
Difficulty: Easy | Medium | Hard
Link: https://www.deep-ml.com/problem/...
"""

def solution(...):
    """
    Brief explanation of approach.
    """
    ...


if __name__ == "__main__":
    # test cases
    ...
```

---

## Progress

### Easy
- [ ] Matrix times vector
- [ ] Transpose of a matrix
- [ ] Reshape matrix
- [ ] Calculate mean by row or column
- [ ] Scalar multiplication of a matrix
- [ ] Matrix multiplication
- [ ] Matrix transformation

### Medium
- [ ] Calculate covariance matrix
- [ ] Linear regression using normal equation
- [ ] Determinant of a 4×4 matrix (Laplace expansion)
- [ ] Calculate eigenvalues of a 2×2 matrix
- [ ] Matrix inverse (2×2)

### Hard
- [ ] Singular value decomposition (SVD)
- [ ] Principal component analysis (PCA)
- [ ] Implement QR decomposition

---

## Key Concepts & Notes

Study notes and teach-back summaries are maintained in [`notes/consolidation.md`](notes/consolidation.md).

### Topics covered

**3B1B — Geometric intuition**
- Linear transformations, determinants, dot product duality, cross products, eigenvalues, change of basis

**MIT 18.06 — Algebraic rigor**
- Gaussian elimination, LU decomposition, four fundamental subspaces, orthogonality, projections, SVD

---

## Commit Convention

```
solve: <problem name> (deep-ml <difficulty> #N)
notes: <topic> consolidation
fix: <problem name> edge case
```

Example: `solve: matrix vector product (deep-ml easy #1)`
