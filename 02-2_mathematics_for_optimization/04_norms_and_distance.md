# Norms and Distance

<style>
table { margin-left: 0 !important; margin-right: auto !important; }
th, td { text-align: left !important; }
.katex .textbb { font-style: italic; }
</style>

**A norm measures vector size; the norm of a difference measures distance.**

Part 2 used vector lengths in cosine similarity. We now explain length, squared length, and distance using the same displacement $𝕕=(1,-1)^{\mathsf T}$.

## 1 · Vector length

For the displacement $𝕕=(1,-1)^{\mathsf T}$ along perpendicular axes with the same unit, the Pythagorean rule gives its length:

$$
\lVert𝕕\rVert_2=\sqrt{1^2+(-1)^2}=\sqrt2.
$$

This length is the **Euclidean norm**. The double bars denote a norm, and the subscript 2 identifies this rule. For any two-component vector $𝕕=(d_1,d_2)^{\mathsf T}$,

$$
\lVert𝕕\rVert_2=\sqrt{d_1^2+d_2^2}.
$$

A norm is nonnegative and equals zero only for the zero vector. Adding the signed components would give $1+(-1)=0$, which would miss the size of this displacement.

## 2 · Distance and squared length

Use positions $𝕩=(3,2)^{\mathsf T}$ and $𝕪=(4,1)^{\mathsf T}$ in perpendicular axes with the same unit. Subtract the positions first, then calculate the length:

$$
\lVert𝕪-𝕩\rVert_2=\sqrt{(4-3)^2+(1-2)^2}=\sqrt2.
$$

An inner product with the same vector gives its **squared length**:

$$
𝕕^{\mathsf T}𝕕=1^2+(-1)^2=2=\lVert𝕕\rVert_2^2.
$$

Length and squared length differ: here they are $\sqrt2$ and 2.

## 3 · Unit vectors

A **unit vector** has length 1. Divide a nonzero vector by its length to keep its direction and set its length to 1:

$$
𝕖=\frac{𝕕}{\lVert𝕕\rVert_2}
=\begin{bmatrix}1/\sqrt2\\-1/\sqrt2\end{bmatrix}.
$$

Checking the length gives $\lVert𝕖\rVert_2=\sqrt{1/2+1/2}=1$. The zero vector cannot be divided by its length because that would divide by zero.

## 4 · Check the calculation

Change only the second component of $𝕕=(1,-1)^{\mathsf T}$ from $-1$ to $-2$.

1. Find the squared length and length of $𝕕=(1,-2)^{\mathsf T}$.
2. Could the length be $-1$, the sum of its components?

**Solution.**

1. Square the components and add, then take the square root for length:

$$
𝕕^{\mathsf T}𝕕=1^2+(-2)^2=5,
\qquad \lVert𝕕\rVert_2=\sqrt5.
$$

2. No. Length cannot be negative. Squaring the components prevents opposite signs from canceling.
