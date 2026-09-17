# 02-2 · Part 2: Inner Products

<style>
table { margin-left: 0 !important; margin-right: auto !important; }
th, td { text-align: left !important; }
.katex .textbb { font-style: italic; }
</style>

**An inner product combines matching vector components into one scalar.**

Part 1 introduced positions $𝕩=(3,2)^{\mathsf T}$ and $𝕪=(4,1)^{\mathsf T}$, with displacement $𝕕=𝕪-𝕩=(1,-1)^{\mathsf T}$. We keep these vectors, calculate weighted sums, and use inner products to compare directions.

## 1 · Multiply matching components and add

The Euclidean **inner product**, also called the dot product, multiplies matching components and adds the results. For $𝕩=(3,2)^{\mathsf T}$ and $𝕕=(1,-1)^{\mathsf T}$,

$$
𝕩^{\mathsf T}𝕕=3(1)+2(-1)=1.
$$

The result is one scalar. For two vectors with $p$ components, the same calculation is

$$
𝕩^{\mathsf T}𝕕=\sum_{i=1}^{p}x_id_i.
$$

Here $i=1,\ldots,p$ indexes matching positions. The shapes are $(1\times p)(p\times1)$; the vectors must have the same number of components.

## 2 · Order, scaling, and sums

Reversing the order of a real inner product gives the same value: $𝕕^{\mathsf T}𝕩=𝕩^{\mathsf T}𝕕=1$.

Keep $𝕩$ fixed and scale $𝕕$:

$$
𝕩^{\mathsf T}(2𝕕)=2,
\qquad 𝕩^{\mathsf T}(-𝕕)=-1.
$$

For $𝕪=(4,1)^{\mathsf T}$, direct calculation gives $𝕩^{\mathsf T}𝕪=3(4)+2(1)=14$. We can also use $𝕪=𝕩+𝕕$ and calculate the two contributions separately:

$$
𝕩^{\mathsf T}𝕪
=𝕩^{\mathsf T}𝕩+𝕩^{\mathsf T}𝕕
=13+1=14.
$$

An inner product distributes over a vector sum: both calculations give 14.

## 3 · An inner product as a weighted sum

Let $𝕨=(2,1)^{\mathsf T}$ be fixed weights. These weights count the first component twice:

$$
𝕨^{\mathsf T}𝕩=2(3)+1(2)=8,
\qquad 𝕨^{\mathsf T}𝕪=2(4)+1(1)=9.
$$

For an input with components $x_1,x_2$, the rule is $𝕨^{\mathsf T}𝕩=2x_1+x_2$. The first component increases by 1 from $𝕩$ to $𝕪$; the second decreases by 1. The weighted change is

$$
𝕨^{\mathsf T}𝕕=2(1)+1(-1)=1.
$$

This matches $9-8=1$. The weights stay fixed; only the input vector changes.

## 4 · Cosine similarity: compare directions

An inner product depends on both vector lengths and their directions. **Cosine similarity** removes the effect of length by dividing by the two vector lengths.

The notation $\lVert𝕕\rVert_2$ means Euclidean length. For $𝕕=(1,-1)^{\mathsf T}$, the Pythagorean rule gives $\lVert𝕕\rVert_2=\sqrt{1^2+(-1)^2}=\sqrt2$. Doubling the vector doubles its length, so $\lVert2𝕕\rVert_2=2\sqrt2$.

Compare $𝕕$ with $2𝕕=(2,-2)^{\mathsf T}$:

$$
\frac{𝕕^{\mathsf T}(2𝕕)}{\lVert𝕕\rVert_2\lVert2𝕕\rVert_2}
=\frac{1(2)+(-1)(-2)}{\sqrt2(2\sqrt2)}=\frac44=1.
$$

The value 1 means that the vectors point in the same direction, even though their lengths differ.

For any two nonzero real vectors of the same dimension, the formula is

$$
\operatorname{cosSim}(𝕩,𝕪)
=\frac{𝕩^{\mathsf T}𝕪}{\lVert𝕩\rVert_2\lVert𝕪\rVert_2}
=\cos\theta,
$$

where $\theta$ is the angle between their directions. The result lies between $-1$ and 1:

| Cosine similarity | Direction comparison |
|:---|:---|
| $1$ | Same direction: $0^\circ$ |
| $0$ | Perpendicular directions: $90^\circ$ |
| $-1$ | Opposite directions: $180^\circ$ |

Cosine similarity is undefined if either vector is zero, because the denominator is then zero.

## 5 · Check the calculation

Keep $𝕩=(3,2)^{\mathsf T}$ fixed. Compare it with the reversed vector $-𝕩=(-3,-2)^{\mathsf T}$.

1. Calculate $𝕩^{\mathsf T}(-𝕩)$.
2. Find their cosine similarity. What does the sign mean?

**Solution.**

1. Multiply matching components and add:

$$
𝕩^{\mathsf T}(-𝕩)=3(-3)+2(-2)=-13.
$$

2. Both vectors have length $\sqrt{3^2+2^2}=\sqrt{13}$. Dividing by the lengths gives

$$
\operatorname{cosSim}(𝕩,-𝕩)=\frac{-13}{\sqrt{13}\sqrt{13}}=-1.
$$

Here the value $-1$ means exactly opposite directions. Reversing the vector changes its direction but keeps its length.
