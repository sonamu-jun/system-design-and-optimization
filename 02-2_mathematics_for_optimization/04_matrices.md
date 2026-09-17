# 02-2 · Part 4: Matrices

<style>
table { margin-left: 0 !important; margin-right: auto !important; }
th, td { text-align: left !important; }
.katex .textbb { font-style: italic; }
</style>

**A matrix groups several component calculations into one vector calculation.**

We keep the input $𝕩=(3,2)^{\mathsf T}$ from the earlier parts. Each matrix row supplies an inner product, so two input components can produce three output components.

## 1 · Shape and matrix-vector multiplication

A **matrix** is a rectangular array of numbers. Here $A$ has three rows and two columns, and the input $𝕩$ has two components:

$$
A=\begin{bmatrix}2&1\\0&3\\1&-1\end{bmatrix},
\qquad 𝕩=\begin{bmatrix}3\\2\end{bmatrix}.
$$

To calculate the output $𝕫=A𝕩$, multiply each row by the input components and add:

$$
𝕫=\begin{bmatrix}2(3)+1(2)\\0(3)+3(2)\\1(3)-1(2)\end{bmatrix}
=\begin{bmatrix}8\\6\\1\end{bmatrix}.
$$

Each output component is one inner product. The shapes are $(3\times2)(2\times1)=(3\times1)$: two inputs produce three outputs. The first row uses the weights $(2,1)$ from Part 2.

In general, $A\in\mathbb R^{m\times p}$ has $m$ rows and $p$ columns. It takes $p$ input components and produces $m$ output components. Its entry $A_{ij}$ lies in row $i$, column $j$, for $i=1,\ldots,m$ and $j=1,\ldots,p$. For example, $A_{12}=1$ is in row 1, column 2.

## 2 · Addition, scaling, and transpose

Add matrices entry by entry when their shapes match. Scalar multiplication multiplies every entry. For example,

$$
A+A=2A=\begin{bmatrix}4&2\\0&6\\2&-2\end{bmatrix}.
$$

The **transpose** exchanges rows and columns:

$$
A^{\mathsf T}=\begin{bmatrix}2&0&1\\1&3&-1\end{bmatrix}.
$$

Thus $A^{\mathsf T}$ has shape $2\times3$. The entry $A_{12}=1$ becomes $(A^{\mathsf T})_{21}=1$.

## 3 · Matrix products and identity

A matrix product combines two calculations. Let $B=\begin{bmatrix}1&0\\0&2\end{bmatrix}$ double the second input component. It changes our input from $(3,2)^{\mathsf T}$ to $B𝕩=(3,4)^{\mathsf T}$. Applying $A$ to this new input gives $(10,12,-1)^{\mathsf T}$.

The product $AB$ does both steps in one multiplication:

$$
AB=\begin{bmatrix}2&2\\0&6\\1&-2\end{bmatrix},
\qquad (AB)𝕩=\begin{bmatrix}10\\12\\-1\end{bmatrix}.
$$

For example, $(AB)_{12}=2(0)+1(2)=2$. Each product entry uses one row from $A$ and one column from $B$.

For $AB$ to exist, the columns of $A$ must match the rows of $B$. Here $(3\times2)(2\times2)$ is valid, but $BA$ is undefined because $(2\times2)(3\times2)$ has mismatched inner dimensions. Order matters.

The **identity matrix** has ones on its diagonal and zeros elsewhere. It leaves a vector unchanged:

$$
I_2=\begin{bmatrix}1&0\\0&1\end{bmatrix},
\qquad I_2𝕩=𝕩.
$$

## 4 · Reading vector inequalities

Suppose each output has an upper limit. Collect the limits in $𝕓=(10,5,2)^{\mathsf T}$. The notation $A𝕩\le𝕓$ compares matching components. For our matrix, it requires all three inequalities:

$$
2x_1+x_2\le10,\qquad 3x_2\le5,\qquad x_1-x_2\le2.
$$

At the original input $𝕩=(3,2)^{\mathsf T}$, we calculated $A𝕩=(8,6,1)^{\mathsf T}$:

| Component | Comparison | Satisfied? |
|:---|:---|:---|
| First | $8\le10$ | Yes |
| Second | $6\le5$ | No |
| Third | $1\le2$ | Yes |

The vector inequality is false because the second component exceeds its limit. **Every component must satisfy its own inequality.** A vector equality, such as $A𝕩=𝕓$, similarly requires equality in every component.

## 5 · Check the calculation

Keep $A$ and $𝕓=(10,5,2)^{\mathsf T}$ fixed. Change only the first component of $𝕩$ from 3 to 4, so $𝕩=(4,2)^{\mathsf T}$.

1. Calculate $A𝕩$.
2. Which output exceeds its limit?

**Solution.**

1. Use the same row calculations with the new first component:

$$
A𝕩=\begin{bmatrix}2(4)+1(2)\\0(4)+3(2)\\1(4)-1(2)\end{bmatrix}
=\begin{bmatrix}10\\6\\2\end{bmatrix}.
$$

2. The second output exceeds its limit: $6>5$. The other comparisons, $10\le10$ and $2\le2$, hold. One failed comparison makes $A𝕩\le𝕓$ false. The second output stays at 6 because it depends only on $x_2$, which is still 2.
