# 02-2 · Notation: Sets, Domains, and Basic Statistics

<style>
table { margin-left: 0 !important; margin-right: auto !important; }
th, td { text-align: left !important; }
.katex .textbb { font-style: italic; }
</style>

**Sets describe collections of numbers; probability and statistics describe uncertain values.**

Lecture 02-1 used these symbols in problem formulations. Here we explain them with small numerical examples.

## 1 · Sets and intervals

A **set** is a collection of distinct elements. $\mathbb R$ is the set of real numbers, and $\mathbb Z$ is the set of integers. Order does not matter: $\{1,2\}=\{2,1\}$.

| Notation | Meaning |
|:---|:---|
| $A=\{0,1,2\}$ | A set with three elements |
| $1\in A$, $3\notin A$ | 1 belongs to $A$; 3 does not |
| $A\subseteq\mathbb R$ | Every element of $A$ is real |
| $A\cap\{2,3\}=\{2\}$ | Intersection: elements in both sets |
| $A\cup\{2,3\}=\{0,1,2,3\}$ | Union: elements in either set |
| $A\cap\{3\}=\varnothing$ | The empty set has no elements |

An **interval** contains every real number between its endpoints. A square bracket includes an endpoint; a parenthesis excludes it.

| Interval | Condition |
|:---|:---|
| $[0,2]$ | $0\le x\le2$ |
| $(0,2)$ | $0<x<2$ |
| $[0,2)$ | $0\le x<2$ |
| $(0,2]$ | $0<x\le2$ |

For example, $1.5\in[0,2]$ but $1.5\notin A$. A set can also be defined by a condition:

$$
[0,2]=\{x\in\mathbb R:0\le x\le2\}.
$$

The colon means “such that.”

## 2 · Ordered pairs and domains

An ordered pair keeps two coordinates in a fixed order. The Cartesian product $\times$ forms all pairs from two sets:

$$
\{0,1\}\times\{2,3\}=\{(0,2),(0,3),(1,2),(1,3)\}.
$$

$\mathbb R^2$ is the set of all ordered pairs of real numbers. A **domain** is a set of allowed inputs. For example,

$$
\mathcal X=[0,2]^2=[0,2]\times[0,2].
$$

Both coordinates must lie in $[0,2]$: $(1,2)\in\mathcal X$, but $(1,3)\notin\mathcal X$. The superscript 2 counts coordinates.

For coordinates $x_1=1$ and $x_2=3$, compare the quantifiers:

| Symbol | Statement | Result |
|:---|:---|:---|
| $\forall$: for every | $\forall i\in\{1,2\},\;x_i\le2$ | False: $x_2=3$ |
| $\exists$: there exists | $\exists i\in\{1,2\}:\;x_i\le2$ | True: $x_1=1$ |

## 3 · Mean of observed values

A **sample** contains observed values. Suppose four observations are $0,4,4,4$. The **sample mean** adds them and divides by their number:

$$
\bar z=\frac{0+4+4+4}{4}=3.
$$

The symbol $\bar z$ denotes the sample mean. Each observation has equal weight.

## 4 · Probability and expectation

Suppose each observation can be either 0 or 4, but 0 is more likely. A **random variable** $X$ represents this uncertain value. Its **distribution** lists the possible values and their probabilities:

| Value $x_i$ | Probability $p_i$ |
|:---|:---|
| 0 | $3/4$ |
| 4 | $1/4$ |

Here $i=1,2$ indexes the rows. Probabilities are nonnegative and sum to 1. The notation $\mathbb P(X=4)=1/4$ means that the probability of the value 4 is $1/4$.

The **expectation** is an average weighted by these probabilities. Multiply each value by its probability and add:

$$
\frac34(0)+\frac14(4)=1.
$$

Simply averaging the two possible values gives $(0+4)/2=2$. This ignores that 0 is three times as likely as 4.

We write the expectation as $\mu$ or $\mathbb E[X]$. The symbol $\sum$ adds the terms over the stated index range:

$$
\mu=\mathbb E[X]=\sum_{i=1}^{2}p_ix_i=1.
$$

The sample mean above is 3, while the expectation is 1. A small sample need not contain values in the same proportions as the distribution.

## 5 · Variance and standard deviation

**Variance** measures spread around the mean. Subtract the mean, square each difference, and average using the same probabilities. Here $\mu=1$, so

$$
\frac34(0-1)^2+\frac14(4-1)^2
=\frac34+\frac94=3.
$$

We write this calculation as

$$
\sigma^2=\operatorname{Var}(X)=\sum_{i=1}^{2}p_i(x_i-\mu)^2.
$$

Squaring prevents positive and negative differences from canceling. The **standard deviation** is the square root of variance:

$$
\sigma=\sqrt{\sigma^2}=\sqrt3.
$$

Variance has squared units; standard deviation has the same units as $X$.

## 6 · Check the calculation

Change only the last observation in $0,4,4,4$ from 4 to 0. Keep the distribution above fixed.

1. Find the new sample mean.
2. Does the expectation change? Explain briefly.

**Solution.**

1. The observations are now $0,4,4,0$, so the sample mean is

$$
\bar z=\frac{0+4+4+0}{4}=2.
$$

2. The expectation stays at $\mathbb E[X]=1$. The distribution's values and probabilities have not changed. Only the observations used for the sample mean have changed.
