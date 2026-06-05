# Consolidation Notes

Running notes from study sessions — teach-back summaries and key insights.

---

## 3B1B — Essence of Linear Algebra

### Ch 7 — Inverse matrices, column space, null space

$Ax = v$ may have no solution when $\det(A) = 0$ (non-invertible), but a solution *can* still exist
if $v$ happens to lie in the column space of $A$ — i.e. $v$ is a linear combination of $A$'s columns.

### Ch 9 — Dot products and duality

The dot product has a dual interpretation via linear transformations:
- Dotting with a **unit vector** $\hat{u}$ = project $v$ onto $\hat{u}$ and take the signed length.
- Dotting with a **non-unit vector** $u$ = project onto $u$'s direction, then scale that length by $\|u\|$.

**Duality:** any linear transformation from $\mathbb{R}^n$ -> $\mathbb{R}$ has a corresponding vector in $\mathbb{R}^n$ such that
applying the transformation is equivalent to taking a dot product with that vector.

The symmetry argument: projection of $\hat{i}$ onto $\hat{u}$ equals projection of $\hat{u}$ onto $\hat{i}$
because bisecting the angle between them, the perpendicular dropped from each onto the other
subtends the same angle. This is why the transformation matrix [u_x, u_y] and the dot product
with $\hat{u}$ are the same operation.

For non-unit vectors: scaling $\hat{u}$ by $t$ scales both components $u_x$ and $u_y$ by $t$,
so the transformation matrix becomes $[tu_x, tu_y]$ — equivalent to projecting then scaling by $t$.

Duality is mind-blowing! 
**Video Transcript Snippet:**
This is why taking the dot product with a unit vector can be interpreted as projecting a vector onto the span of that unit vector and taking the length. This is why the dot product with a non-unit vector can be interpreted as first projecting onto that vector, then scaling up the length of that projection by the length of the vector.


### Ch 10 — Cross products

The cross product $p = v \times w$ is defined by the property:

    p · [x, y, z] = det([[x, v_x, w_x], [y, v_y, w_y], [z, v_z, w_z]])

Geometrically: this determinant equals the signed volume of the parallelepiped formed by
[x,y,z], v, and w — which equals the area of the v-w parallelogram times the component of
[x,y,z] perpendicular to it.

**Derivation of p from duality:**
- The determinant is a linear function of [x,y,z], so by duality a vector p must exist
- Volume = base area × height = area(v,w) × (component of [x,y,z] perpendicular to v-w plane)
- For p·[x,y,z] to replicate this: p must point perpendicular to v and w (to extract the height
  component), and have magnitude equal to the area of the v-w parallelogram (to scale correctly)
- This uniquely defines p = v × w

**Throughline across Ch 7, 9, 10:** duality — the column space condition, dot-product-as-functional,
and determinant-as-dot-product are all the same idea in different forms.

**Video Transcript Snippet:**
What vector p has the special property that when you take a dot product between p and some vector x, y, z, it gives the same result as plugging in x, y, z to the first column of a matrix whose other two columns have the coordinates of v and w, then computing the determinant. What 3D vector p has the special property that when you take a dot product between p and some other vector x, y, z, it gives the same result as if you took the signed volume of a parallelepiped defined by this vector x, y, z along with v and w. Start by taking the area of the parallelogram defined by v and w, then multiply it not by the length of x, y, z, but by the component of x, y, z that's perpendicular to that parallelogram.

### Ch 6 — The determinant

The determinant measures the signed scaling factor of area under a linear transformation.

**Why ad - bc:** The parallelogram formed by transformed basis vectors lives inside a bounding
rectangle of side (a+b) × (c+d). Subtracting the corner pieces:
    (a+b)(c+d) - 2bc - ac - bd = ad - bc

**Why negative:** encodes orientation flip — positive if $\hat{i}$ remains to the left of $\hat{j}$
(same handedness), negative if they swap. Example: [[0,1],[1,0]] reflects across y=x, det = -1.

Since any region decomposes into tiny unit squares each scaled by the same factor, the determinant
applies universally to any area, not just the unit square.

---

## MIT 18.06 — Gilbert Strang

### LU Decomposition (L1–L4)

Gaussian elimination does two things simultaneously: factors A into LU, and solves for x given b.

**Why LU matters:** Pay the $O(n^3)$ factorization cost once. For each new right-hand side b, only
need forward substitution $Lc = b$ then back substitution Ux = c — both $O(n^2)$. For k right-hand
sides: $O(n^3) + k·O(n^2)$ vs $k·O(n^3)$ without LU.

**Forward substitution (Lc = b):** L is lower triangular — solve top to bottom, each row
introduces exactly one new unknown.

**Back substitution (Ux = c):** U is upper triangular — solve bottom to top, same reason.

### Null space and rank (L6–L8)

When elimination hits a zero pivot, the system is rank-deficient:
- **r < m** (fewer pivots than rows): not every b is reachable — zero pivot row imposes a
  consistency condition on b. No solution when that condition fails.
- **r < n** (fewer pivots than columns): free variables exist, null space is non-trivial.
  Infinitely many solutions when a solution exists.

**Special solutions:** setting each free variable to 1 one at a time (rest to 0) gives n-r
special solutions. These are linearly independent by construction — each has a 1 in exactly
one free variable position where all others have 0. They form a basis for the null space.

**Rank-nullity theorem:** r + (n - r) = n (pivot variables + null space dimension = total dimensions)

### Four fundamental subspaces (L9–L11)

For an m×n matrix of rank r:

| Subspace | Dimension | Lives in |
|---|---|---|
| Row space | r | $\mathbb{R}^n$ |
| Null space | n - r | $\mathbb{R}^n$ |
| Column space | r | $\mathbb{R}^m$ |
| Left null space | m - r | $\mathbb{R}^m$ |

**Row space and null space are orthogonal complements in $\mathbb{R}^n$:**
1. Orthogonality: Ax = 0 means every row dotted with any null space vector = 0. Extends to all
   row space vectors by linearity (linear combinations of rows are also orthogonal to null space).
2. Complements: orthogonality rules out overlap; dimensions adding to n rules out gaps. Together
   they guarantee every vector in $\mathbb{R}^n$ decomposes uniquely as x = x_row + x_null.

**Row rank = column rank = r:** elimination produces a fixed number of pivots, which simultaneously
counts independent rows and independent columns. Same pivot count, different perspectives.
