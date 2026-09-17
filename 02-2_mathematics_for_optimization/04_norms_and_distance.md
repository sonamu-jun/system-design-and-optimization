# Norms and Distance

<style>
table { margin-left: 0 !important; margin-right: auto !important; }
th, td { text-align: left !important; }
.katex .textbb { font-style: italic; }
</style>

**A norm measures vector size; the norm of a difference measures distance.**

The inner products chapter used vector lengths in cosine similarity. We now compare the 1-, 2-, 3-, and infinity norms, then explain squared length and distance using the same displacement $𝕕=(1,-1)^{\mathsf T}$.

## 1 · Vector length and the 2-norm

For the displacement $𝕕=(1,-1)^{\mathsf T}$ along perpendicular axes with the same unit, the Pythagorean rule gives its length:

$$
\lVert𝕕\rVert_2=\sqrt{1^2+(-1)^2}=\sqrt2.
$$

This length is the **Euclidean norm**, also called the **2-norm**. The double bars denote a norm, and the subscript 2 identifies this rule. For any two-component vector $𝕕=(d_1,d_2)^{\mathsf T}$,

$$
\lVert𝕕\rVert_2=\sqrt{d_1^2+d_2^2}.
$$

A norm is nonnegative and equals zero only for the zero vector. Adding the signed components would give $1+(-1)=0$, which would miss the size of this displacement.

## 2 · Compare the 1-, 2-, 3-, and infinity norms

Different norms measure the size of the same vector using different rules. For a real vector $𝕕$ with $p$ components, $d_i$ is component $i$, where $i=1,\ldots,p$. The notation $\lvert d_i\rvert$ means absolute value, so $\lvert-1\rvert=1$.

Keep $𝕕=(1,-1)^{\mathsf T}$ fixed and change only the norm:

| Norm | Definition | Calculation for $𝕕=(1,-1)^{\mathsf T}$ |
|:---|:---|:---|
| 1-norm | $\lVert𝕕\rVert_1=\sum_{i=1}^{p}\lvert d_i\rvert$ | $1+1=2$ |
| 2-norm | $\lVert𝕕\rVert_2=\left(\sum_{i=1}^{p}\lvert d_i\rvert^2\right)^{1/2}$ | $\sqrt{1^2+1^2}=\sqrt2$ |
| 3-norm | $\lVert𝕕\rVert_3=\left(\sum_{i=1}^{p}\lvert d_i\rvert^3\right)^{1/3}$ | $\sqrt[3]{1^3+1^3}=\sqrt[3]{2}$ |
| Infinity norm | $\lVert𝕕\rVert_{\infty}=\max_{1\le i\le p}\lvert d_i\rvert$ | $\max(1,1)=1$ |

The 1-norm adds absolute component values. The 2-norm squares them, adds, and takes the square root. The 3-norm cubes them, adds, and takes the cube root. **Take absolute values before cubing** so opposite signs do not cancel.

The infinity norm takes the largest absolute component. The subscript $\infty$ names this rule; it does not mean that the result is infinite. These four values differ even though the displacement is unchanged. Only the 2-norm gives the usual straight-line length along perpendicular axes with the same unit.

## 3 · Distance and squared length

Use positions $𝕩=(3,2)^{\mathsf T}$ and $𝕪=(4,1)^{\mathsf T}$ in perpendicular axes with the same unit. Subtract the positions first, then calculate the length:

$$
\lVert𝕪-𝕩\rVert_2=\sqrt{(4-3)^2+(1-2)^2}=\sqrt2.
$$

An inner product with the same vector gives its **squared length**:

$$
𝕕^{\mathsf T}𝕕=1^2+(-1)^2=2=\lVert𝕕\rVert_2^2.
$$

Length and squared length differ: here they are $\sqrt2$ and 2. In $\lVert𝕕\rVert_2^2$, the subscript 2 selects the norm and the superscript 2 squares its value.

## 4 · Unit vectors

A **unit vector** here has Euclidean length 1. Divide a nonzero vector by its 2-norm to keep its direction and set its length to 1:

$$
𝕖=\frac{𝕕}{\lVert𝕕\rVert_2}
=\begin{bmatrix}1/\sqrt2\\-1/\sqrt2\end{bmatrix}.
$$

Checking the length gives $\lVert𝕖\rVert_2=\sqrt{1/2+1/2}=1$. The zero vector cannot be divided by its length because that would divide by zero.
