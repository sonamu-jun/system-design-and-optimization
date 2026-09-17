# Vectors and Displacements

<style>
table { margin-left: 0 !important; margin-right: auto !important; }
th, td { text-align: left !important; }
.katex .textbb { font-style: italic; }
</style>

**A vector stores numbers in a fixed order and supports component-by-component arithmetic.**

The notation guide introduced ordered pairs. We now write them as vectors, distinguish position from relative displacement, and calculate sums, differences, and scalar multiples.

## 1 · Scalars, vectors, and order

A **scalar** is one number. A **vector** is an ordered collection of numbers called components. For example,

$$
𝕩=\begin{bmatrix}3\\2\end{bmatrix},
\qquad x_1=3,\quad x_2=2.
$$

Italic double-struck letters such as $𝕩$ denote vectors; ordinary letters such as $x_1$ denote scalar components.

Two vectors are equal when all matching components agree. Order matters:

$$
\begin{bmatrix}3\\2\end{bmatrix}\ne\begin{bmatrix}2\\3\end{bmatrix}.
$$

## 2 · Dimension and transpose

Our vector has two real components, so we write $𝕩\in\mathbb R^2$. Its **dimension** is 2. The zero vector $𝟘=\begin{bmatrix}0\\0\end{bmatrix}$ also has dimension 2.

We use column vectors. The **transpose** symbol $\mathsf T$ changes a column into a row:

$$
𝕩=\begin{bmatrix}3\\2\end{bmatrix},
\qquad 𝕩^{\mathsf T}=\begin{bmatrix}3&2\end{bmatrix}.
$$

The shapes are $2\times1$ and $1\times2$: rows first, then columns. The notation $(3,2)^{\mathsf T}$ is a compact column vector.

More generally, $𝕩\in\mathbb R^p$ means that $𝕩$ has $p$ real components, indexed by $i=1,\ldots,p$:

$$
𝕩=\begin{bmatrix}x_1\\\vdots\\x_p\end{bmatrix}.
$$

Here $p$ is the dimension, and the vertical dots stand for the intervening components.

## 3 · Position vectors

To describe where a point is, choose an origin $O$ and coordinate axes. In a two-dimensional coordinate system, let $P$ have coordinates $(3,2)$ and $Q$ have coordinates $(4,1)$.

A **position vector** points from the chosen origin to a point:

$$
𝕩=\overrightarrow{OP}=\begin{bmatrix}3\\2\end{bmatrix},
\qquad
𝕪=\overrightarrow{OQ}=\begin{bmatrix}4\\1\end{bmatrix}.
$$

The point $P$ is a location; $𝕩$ describes that location relative to $O$. These coordinate pairs are the same vectors used above, now interpreted as positions. A vector can also store quantities other than position, such as two cooling decisions.

## 4 · Relative vectors and displacement

How far, and in which direction, is $Q$ from $P$? The **relative vector of $Q$ with respect to $P$** points from $P$ to $Q$. Subtract the starting position from the ending position, component by component:

$$
𝕕=\overrightarrow{PQ}=𝕪-𝕩
=\begin{bmatrix}4-3\\1-2\end{bmatrix}
=\begin{bmatrix}1\\-1\end{bmatrix}.
$$

This is the **displacement** from $P$ to $Q$: the first coordinate increases by 1 and the second decreases by 1. Adding it to the starting position recovers the ending position:

$$
𝕩+𝕕=\begin{bmatrix}3+1\\2-1\end{bmatrix}
=\begin{bmatrix}4\\1\end{bmatrix}=𝕪.
$$

Reversing the reference reverses the direction: the relative vector of $P$ with respect to $Q$ is $𝕩-𝕪=-𝕕=(-1,1)^{\mathsf T}$. Vector addition and subtraction require matching dimensions.

Now keep the points, axis directions, and units fixed, but move the origin to the old coordinates $(1,1)$. The new coordinates of $P$ and $Q$ are $(2,1)$ and $(3,0)$. Their difference is still

$$
\begin{bmatrix}3-2\\0-1\end{bmatrix}
=\begin{bmatrix}1\\-1\end{bmatrix}=𝕕.
$$

**Changing the origin changes the position vectors, but leaves their relative vector unchanged.**

## 5 · Scalar multiplication

A scalar multiplies every component. For example, doubling $𝕕=(1,-1)^{\mathsf T}$ gives

$$
2𝕕=\begin{bmatrix}2(1)\\2(-1)\end{bmatrix}
=\begin{bmatrix}2\\-2\end{bmatrix}.
$$

For any scalar $\alpha$, the same rule gives $\alpha𝕕=(\alpha,-\alpha)^{\mathsf T}$.

| Multiplier | Result | Meaning |
|:---|:---|:---|
| $2$ | $2𝕕=(2,-2)^{\mathsf T}$ | Twice the size |
| $1/2$ | $\frac12𝕕=(1/2,-1/2)^{\mathsf T}$ | Half the size |
| $-1$ | $-𝕕=(-1,1)^{\mathsf T}$ | Reversed direction |
| $0$ | $0𝕕=𝟘$ | Zero vector |
