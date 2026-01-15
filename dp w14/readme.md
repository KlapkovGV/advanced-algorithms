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

**The Data**

The table in the top right lists the items available for a knapsack with a total capacity W=5

| Item (i) | Weight (w_i) | Value (v_i) |
| :--- | :---: | :---: |
| 1 | 2 | $12 |
| 2 | 1 | $10 |
| 3 | 3 | $20 |
| 4 | 2 | $15 |

**Step-by-Step Calculation**

This shows the manual calculation for the first two items (i = 1 and i = 2) across al possible capacities (j = 1 to 5).

The table is just the input list. In that table:
- i is the row number;
- w and v are just properties of those items.

Row i=1 (item 1: weight 2, value 12)
- at j=1: the capacity is too small for item 1 (1-2 < 0), so the value is 0;
- at j=2 to 5: the capacity fits item 1. Since there are no previous items to compare against, the max value becomes the value of item 1 (12).

To see j=2 to 5, we have to move the input list to the Dynamic Programming table. In a DP table, j represents the capacity of the bag, and it creates the columns. 

We solving this problem for a bag with a maximum capacity of 5, our table would expand to look like this:

| j=0 | j=1 | j=2 | j=3 | j=4 | j=5 |
|-----|-----|-----|-----|-----|-----|
| **i=0** | 0 | 0 | 0 | 0 | 0 | 0 |
| **i=1** | 0 | 0 | 12 | 12 | 12 | 12 |
| **i=2** | 0 | - | - | - | - | - |
| **i=3** | 0 | - | - | - | - | - |
| **i=4** | 0 | - | - | - | - | - |

So dynamic programming is bult on the idea of saving answers to smaller version of our problem.

Row i=2 (item 2: weight 1, value 10)
- at j=1: can we fit item 2? Yes (1 - 1 = 0). Compare the previous row's value (0) vs. item 2's value (10). Result: 10;
- at j=3: can we fit item 2? yes.
  - option A (leave it): look at F(1,3), which is 12;
  - option B (take it): take item 2 (value 10) + whatever fit in the remaining weight (3 - 1 = 2). In the privious row, weight 2 was worth 12. So, 10 + 12 = 22;
  - result: max(12, 22) is 22.
- at j=4: can we fit item 2? yes (4-1)=3.
  - max(F(2-1, 4), 10 + F(2-1, 4-1)) - max(10, 22). Result: 22;
- at j=5: the process is same.

| i | j=0 | j=1 | j=2 | j=3 | j=4 | j=5 |
|-----|-----|-----|-----|-----|-----|-----|
| **i=0** | 0 | 0 | 0 | 0 | 0 | 0 |
| **i=1** | 0 | 0 | 12 | 12 | 12 | 12 |
| **i=2** | 0 | 10 | 22 | 22 | 22 | 22 |
| **i=3** | 0 | - | - | - | - | - |
| **i=4** | 0 | - | - | - | - | - |

Row i=3 (item 3: weight 3, value 20):
- at j=1: can we fit item 3? no (1 - 3 < 0), because the capacity is too small for item 3. Value is 10;
- at j=2: can we fit item 3? no (2 - 3 < 0). So value is from the previous item - 12;
- at j=3: can we fit item 3? yes (3 - 3 = 0). max(F(3-1, 3), 20 + F(3-1, 3-3)) -> max(22, 20). Result: 22;
- at j=4: max(F(3-1, 4), 20 + F(3-1, 4-3)) -> max(22, 30). Result: 30;
- at j=5: max(F(3-1, 5), 20 + F(3-1, 5-3)) -> max(22, 32). Result: 32.

Row i=4 I will fill without explanation.

| i | j=0 | j=1 | j=2 | j=3 | j=4 | j=5 |
|-----|-----|-----|-----|-----|-----|-----|
| **i=0** | 0 | 0 | 0 | 0 | 0 | 0 |
| **i=1** | 0 | 0 | 12 | 12 | 12 | 12 |
| **i=2** | 0 | 10 | 12 | 22 | 22 | 22 |
| **i=3** | 0 | 10 | 12 | 22 | 30 | 32 |
| **i=4** | 0 | 10 | 15 | 25 | 30 | 37 |

**Backtracking phase of the 0/1 Knapsack Problem**

While the previous section explained how to find the maximum value, this section explains how to identify which specific items make up that value.

**1. The Completed DP Table**
- final answer: the value at V(4,5)=37 is the maximum possible value for a knapsack with capacity 5.

**2. Backtracking Logic**

To find the items, we start from the bottom-right (i=4, j=5) and work backwards using this rule:

```math
if V[i,j] > V[i-1,j],
it\ means\ item\ i\ was\ included.
```

If the value is the same as the row above it, the item was skepped.

**Step-by-step breakdown:**
1. Check item 4 (i=4, j=5):
   - is V(4,5) > V(3,5)? yes;
   - action: include item 4. New capacity j=5-2=3.
2. Check item 3 (i=3, j=3):
   - is V(3,3) > V(2,3)? no;
   - action: skip item 3. Capacity remains j=3.
3. Check item 2 (i=2, j=3):
   - is V(2,3) > V(1,3). yes;
   - action: include item 2. New capacity j=3-1=2.
4. Check item 1 (i=1, j=2):
   - is V(1,2) > V(0,2)? yes;
   - action: include item 1. Final capacity j=2-2=0.
  
The list of selected items is 4, 2, and 1.
- total weight: 2 (Item 4) + 1 (Item 2) + 2 (Item 1) = 5;
- total Value: 15 (Item 4) + 10 (Item 2) + 12 (Item 1) = 37.

Items 4, 2, and 1 should be selected.

**Python explanation**
```python
def backtrack(m_list, dp_list):
  i, j = len(dp_list)-1, len(dp_list[0])-1
  backtrack_list = []
  while i >= 0:
     for w in m_list:
      if dp_list[i][j] > dp_list[i-1][j]:
        print(dp_list[i][j])
        j = j - w
        backtrack_list.append(i)
        print(dp_list[i][j])
        i = i - 1   
        print(dp_list[i][j])   
      else:
        j = j
        i = i - 1
  return backtrack_list

dp_list = [
      [0, 0, 0, 0, 0, 0],
      [0, 0, 12, 12, 12, 12],
      [0, 10, 12, 22, 22, 22],
      [0, 10, 12, 22, 30, 32],
      [0, 10, 15, 25, 30, 37]
      ]

m_list = [2, 3, 1, 2]

result = backtrack(m_list, dp_list)
print(result)
```
