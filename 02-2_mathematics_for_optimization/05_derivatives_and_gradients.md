# 02-2 · Part 5: Derivatives and Gradients

<style>
table { margin-left: 0 !important; margin-right: auto !important; }
th, td { text-align: left !important; }
.katex .textbb { font-style: italic; }
</style>

**A derivative measures how a calculated value changes when an input changes.**

We keep the vector $𝕩=(3,2)^{\mathsf T}$ from the earlier parts. We now differentiate simple scalar expressions made from its two components.

## 1 · Two inputs and one output

A **function** assigns one output to each allowed input. For example, square the two components of $𝕩=(3,2)^{\mathsf T}$ and add: $3^2+2^2=13$. We name this calculation $f$ and write its rule as

$$
f(𝕩)=x_1^2+x_2^2.
$$

The input is the vector $𝕩=(x_1,x_2)^{\mathsf T}$, and the output is one number. At our input, $f(𝕩)=13$.

## 2 · A derivative measures a local rate of change

Hold $x_2=2$ and write $q=x_1$. Our calculation becomes $e(q)=q^2+4$. Increasing $q$ from 3 to 3.1 changes the output from 13 to 13.61. Divide the output change by the input change:

$$
\frac{e(3.1)-e(3)}{3.1-3}=\frac{13.61-13}{0.1}=6.1.
$$

This is an **average rate of change**. Keep the starting input at 3 and make the change smaller:

| Input change | Average rate |
|:---|:---|
| $0.1$ | $6.1$ |
| $0.01$ | $6.01$ |

For a starting input $q$ and a nonzero change $h$, this rate is $[e(q+h)-e(q)]/h$. The constant 4 cancels when we subtract the outputs. Expanding the square gives

$$
\begin{aligned}
\frac{e(q+h)-e(q)}{h}
&=\frac{(q+h)^2-q^2}{h}\\
&=\frac{2qh+h^2}{h}=2q+h.
\end{aligned}
$$

Because $h\ne0$, we can divide each term in the numerator by $h$. As $h$ approaches zero from either side, $2q+h$ approaches $2q$. The **derivative** is this limiting rate:

$$
e'(q)=\lim_{h\to0}\frac{e(q+h)-e(q)}{h}=2q.
$$

The prime denotes a derivative, and $\lim_{h\to0}$ means the limit as $h$ approaches zero. At $q=3$, the derivative is $e'(3)=6$. This is a local rate, not the output value $e(3)=13$.

For fixed numbers $a$ and $b$, the basic calculation rules are:

| Expression | Derivative with respect to $q$ |
|:---|:---|
| $b$ | $0$ |
| $aq$ | $a$ |
| $aq^2$ | $2aq$ |

Differentiate sums term by term. Thus $e'(q)=2q+0=2q$: a constant contributes zero.

## 3 · Partial derivatives: change one input

A **partial derivative** measures change in one coordinate while holding the other fixed. At $(3,2)$, holding $x_2=2$ gives the rate $2(3)=6$ from the previous calculation. Holding $x_1=3$ instead gives the rate $2(2)=4$ for changes in $x_2$.

The symbol $\partial$ identifies which coordinate changes. For $f(𝕩)=x_1^2+x_2^2$,

$$
\frac{\partial f}{\partial x_1}=2x_1,
\qquad \frac{\partial f}{\partial x_2}=2x_2.
$$

When differentiating with respect to $x_1$, the term $x_2^2$ is constant. The roles reverse for $x_2$.

## 4 · The gradient collects the partial derivatives

The **gradient** collects the partial derivatives into a column vector in input order. At $(3,2)$, the two rates 6 and 4 become

$$
\nabla f(3,2)=\begin{bmatrix}6\\4\end{bmatrix}.
$$

The symbol $\nabla$ is read “nabla.” At a general input $𝕩$, the same ordering gives

$$
\nabla f(𝕩)
=\begin{bmatrix}\partial f/\partial x_1\\\partial f/\partial x_2\end{bmatrix}
=\begin{bmatrix}2x_1\\2x_2\end{bmatrix}.
$$

The function value 13 is a scalar. Its gradient has two components, one rate for each input. A function with more input components has one partial derivative per component in its gradient.

## 5 · Simple vector differentiation

For a scalar expression, differentiation with respect to a vector means finding its gradient. The notation $\nabla_{𝕩}$ says that $𝕩$ is the variable.

First keep $𝕨=(2,1)^{\mathsf T}$ fixed, as in Part 2:

$$
𝕨^{\mathsf T}𝕩=2x_1+x_2,
\qquad
\nabla_{𝕩}(𝕨^{\mathsf T}𝕩)=\begin{bmatrix}2\\1\end{bmatrix}=𝕨.
$$

Next, let both factors be the variable. Expanding the inner product gives the function we just differentiated:

$$
𝕩^{\mathsf T}𝕩=x_1^2+x_2^2,
\qquad
\nabla_{𝕩}(𝕩^{\mathsf T}𝕩)=\begin{bmatrix}2x_1\\2x_2\end{bmatrix}=2𝕩.
$$

**Both copies of $𝕩$ vary**, so the result is $2𝕩$. Multiplying the expression by $1/2$ cancels this factor:

$$
\nabla_{𝕩}\!\left(\frac12𝕩^{\mathsf T}𝕩\right)=𝕩.
$$

At $𝕩=(3,2)^{\mathsf T}$, these last two gradients are $(6,4)^{\mathsf T}$ and $(3,2)^{\mathsf T}$, respectively.

## 6 · A squared-distance example

Keep the point $𝕪=(4,1)^{\mathsf T}$ from Part 1 fixed. Half the squared distance from $𝕩$ to $𝕪$ is

$$
\ell(𝕩)=\frac12\lVert𝕩-𝕪\rVert_2^2
=\frac12(x_1-4)^2+\frac12(x_2-1)^2.
$$

Expand the squares and differentiate one component at a time:

$$
\ell(𝕩)=\frac12x_1^2-4x_1+8
+\frac12x_2^2-x_2+\frac12,
$$

$$
\nabla_{𝕩}\ell(𝕩)
=\begin{bmatrix}x_1-4\\x_2-1\end{bmatrix}=𝕩-𝕪.
$$

At $𝕩=(3,2)^{\mathsf T}$, $\ell(𝕩)=1$ and its gradient is $(-1,1)^{\mathsf T}$. Increasing $x_1$ a little decreases that value; increasing $x_2$ a little increases it. The signs describe the local effect of each input.

## 7 · Check the calculation

Change only the first component of $𝕩$ from 3 to 4, keeping $x_2=2$. Use $f(𝕩)=𝕩^{\mathsf T}𝕩=x_1^2+x_2^2$.

1. When differentiating with respect to $x_1$, which term is constant?
2. Find the gradients of $f$ and $\frac12f$ at $𝕩=(4,2)^{\mathsf T}$.

**Solution.**

1. Hold $x_2=2$ fixed. The term $x_2^2=4$ is constant, so its derivative with respect to $x_1$ is zero.
2. Differentiate each component while holding the other fixed. This gives

$$
\nabla f(4,2)=\begin{bmatrix}2(4)\\2(2)\end{bmatrix}
=\begin{bmatrix}8\\4\end{bmatrix},
$$

$$
\nabla_{𝕩}\!\left(\frac12f(𝕩)\right)
=\frac12\begin{bmatrix}8\\4\end{bmatrix}
=\begin{bmatrix}4\\2\end{bmatrix}
\quad\text{at }𝕩=(4,2)^{\mathsf T}.
$$

Multiplying the function by $1/2$ halves each partial derivative. Thus the two gradients are $2𝕩$ and $𝕩$.
