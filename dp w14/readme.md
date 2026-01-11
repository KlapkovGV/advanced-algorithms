# Knapsack Problem

- we have n items with known weight values (w1, ..., wn);
- each item has values such as (v1, ..., vn);
- our knapsack has a specific capacity W.

Can we find the most valuable subset? 

A problem of deciding which objects a person will keep:
- it must fit in their bag;
- the value should be as hogh as possible.

![algo](https://github.com/user-attachments/assets/dcfdca89-7f6b-4bbc-be78-d2e775717e59)

### Knapsack Problem Example (Capacity W = 10)

This table demonstrates the brute-force approach to finding the optimal subset of items that maximizes value without exceeding the capacity of 10.

| Subset | Total Weight | Total Value | Status |
| :--- | :---: | :---: | :--- |
| $\varnothing$ | 0 | $0 | Feasible |
| {1} | 7 | $42 | Feasible |
| {2} | 3 | $12 | Feasible |
| {3} | 4 | $40 | Feasible |
| {4} | 5 | $25 | Feasible |
| {1, 2} | 10 | $54 | Feasible |
| {1, 3} | 11 | - | Not feasible |
| {1, 4} | 12 | - | Not feasible |
| {2, 3} | 7 | $52 | Feasible |
| {2, 4} | 8 | $37 | Feasible |
| **{3, 4}** | **9** | **$65** | **Optimal Solution** |
| {1, 2, 3} | 14 | - | Not feasible |
| {1, 2, 4} | 15 | - | Not feasible |
| {1, 3, 4} | 16 | - | Not feasible |
| {2, 3, 4} | 12 | - | Not feasible |
| {1, 2, 3, 4} | 19 | - | Not feasible |

### Logic for a Dynamic Programming approach

To develop a solution based on dynamic programming, a relationship for a smaller-scale subproblem must first be established.

**Recursive formula**

```math
F(i, j) =
\begin{cases}
\max\{F(i - 1, j), \; v_i + F(i - 1, j - w_i)\}, & \text{if } j - w_i \geq 0, \\F(i - 1, j), & \text{if } j - w_i < 0.
\end{cases}
```

**Base Cases**
```math
F(0, j) = 0 \quad \text{for } j \geq 0
```
```math
F(i, 0) = 0 \quad \text{for } i \geq 0
```

### Dynamic Programming Table Structure

This table illustrates the dependency of the current cell $F(i, j)$ on previously calculated values in the dynamic programming matrix.

| | 0 | ... | $j - w_i$ | ... | $j$ | ... | $W$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **...** | 0 | | | | | | |
| **$i-1$** | 0 | | $F(i-1, j-w_i)$ | | $F(i-1, j)$ | | |
| **$i$ ($w_i, v_i$)** | 0 | | | | **$F(i, j)$** | | |
| **...** | 0 | | | | | | |
| **$n$** | 0 | | | | | | **Goal** |

**Legend:**
- **$i$**: Current item being considered.
- **$j$**: Current capacity of the sub-knapsack.
- **$F(i, j)$**: The maximum value achievable using a subset of the first $i$ items with a combined weight $\leq j$.
- **Goal**: The final answer, representing the maximum value for $n$ items and capacity $W$.
