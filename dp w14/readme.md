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

### Pseudocode 
```python
algorithm DPKnapsack(w[1..n], v[1..n], W)
// solves the knapsack problem by dynamic programming (bottom up)
// input: arrays w[1..n] and v[1..n] of weights and values of n items, knapsack capacity W
// output: table v[0..n, 0..W] that contains the value of an optimal subset in V[n, W] and from which the items of an optimal subset can be found
for i <- 0 to n do V[i, 0] <- 0
for j <- 1 to W do V[0, j] <- 0
for i <- 1 to n do
  for j <- 1 to W do
    if j-w[i] >= 0
      V[i, j] <- max{V[i-1, j], v[i] + V[i-1, j-w[i]]}
    else V[i,j] <- V[i-1, j]
return V[n, W], V

algorithm backtrack 
k <- 0 // size of the list of items in an optimal solution
j <- W // unused capacity
for j <- n downto 1 do
  if V[i, j] > V[i-1, j]
    k <- k + 1
    L[k] <- i // include item i
    j <- j - w[i]
return L
```

1. The new problem instance

Apply the bottom-up dynamic programming algorithm using these values:
- Knapsack Capacity (W): 6;
- Items Available

| Item | Weight ($w$) | Value ($v$) |
| :--- | :--- | :--- |
| 1 | 3 | $25 |
| 2 | 2 | $20 |
| 3 | 1 | $15 | 
| 4 | 4 | $40 |
| 5 | 5 | $50 |

2. Conceptual Questions Breakdown

**Question (b): How many different optimal subsets exist?**

An "optimal subset" is a combination of items that reaches the absolute maximum value possible for capacity W=6. Sometimes, two different combinations of items can result in the exact same maximum value. For example, if both (Item 1 + Item 3) and (Item 4) resulted in a value of 40 and both fit in the knapsack, you would have two optimal subsets.

**Question (c): How can the DP table identify multiple optimal solutions?**

In the dynamic programming table, we can tell there is more than one optimal subset if, during the calculation of a cell, there is a tie.
- Recall the formula:
```math
 F(i, j) = \max\{F(i - 1, j), v_i + F(i - 1, j - w_i)\}.
```
- f F(i - 1, j) is exactly equal to v_i + F(i - 1, j - w_i), it means you could either "leave" or "take" the current item and achieve the same value.

![knapsack](https://github.com/user-attachments/assets/b5bfdd97-b1e7-4e53-9371-2c53fe8e02d9)

1. The Completed DP Table
   
The table is filled using the bottom-up approach, where each row represents an item and each column represents a capacity from 0 to 6.

Final Result: The value in the bottom-right cell is 65. This is the maximum value that can be achieved with the given items and capacity.

Item Data:
- Item 1: w=3,v=25
- Item 2: w=2,v=20
- Item 3: w=1,v=15
- Item 4: w=4,v=40
- Item 5: w=5,v=50

2. Backtracking to Find the Optimal Subset

The right side of the image shows the logic used to find which items were picked, starting from the final result V(5,6)=65.

Check Item 5: V(5,6)=65, while the row above it V(4,6)=60. Since 65>60, Item 5 is included.

Remaining capacity: 6−5(weight)=1.

Check Item 4: Move to capacity j=1 in the row above. V(4,1)=15 and V(3,1)=15. Since they are equal (15=15), Item 4 is NOT included.

Check Item 3: Still at capacity j=1. V(3,1)=15 while V(2,1)=0. Since 15>0, Item 3 is included.

Remaining capacity: 1−1(weight)=0.

The optimal subset is {Item 5, Item 3}.

3. Answering the Conceptual Questions
Based on this table, we can now answer the questions from the previous slide:

Part (b) How many optimal subsets?: There is only one optimal subset ({5, 3}) because the maximum value 65 only appears once in the final row.

Part (c) Identifying multiple solutions: You can tell there is more than one optimal solution if you encounter a tie during backtracking. For example, if V[i,j] was exactly equal to v_i+V[i−1,j−w_i], you would have two different paths to follow, leading to two different but equally optimal sets of items.

# A different algorithmic concept: Kadane’s Algorithm for the Maximum Subarray Sum problem

Core Concept

Given an integer array arr[], we must find a contiguous subarray (a slice of the array where elements are next to each other) that results in the highest total sum.

Examples Provided

The image gives three examples to illustrate how the algorithm works:

<img width="752" height="227" alt="image" src="https://github.com/user-attachments/assets/0be680e2-fa7e-4731-bc15-69bf537a5204" />

<img width="599" height="307" alt="image" src="https://github.com/user-attachments/assets/a56fb9c4-5e1d-4611-adc8-b339f7d8c7db" />

<img width="602" height="305" alt="image" src="https://github.com/user-attachments/assets/f03ea23c-16fb-4536-98b7-5015278ec0bb" />


<img width="588" height="301" alt="image" src="https://github.com/user-attachments/assets/ad956ff1-1c89-42eb-847d-4deedbf61d4b" />

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/5c2e6e8e-0011-4935-b41f-2bcb1e2281db" />

<img width="590" height="298" alt="image" src="https://github.com/user-attachments/assets/4dda04f7-e5d1-4f03-84b8-b7107ffd4111" />

<img width="599" height="302" alt="image" src="https://github.com/user-attachments/assets/c180b8f5-c2a9-4929-8855-52440605a5c9" />

<img width="596" height="296" alt="image" src="https://github.com/user-attachments/assets/1a466323-4ade-49cc-9ae2-dfbb8d9d1aeb" />

# The Rod Cutting Problem, another classic optimization challenge solved using Dynamic Programming

1. The Core Concept

The goal is to take a rod of length $n$ and determine the best way to cut it into smaller pieces to maximize the total sale price. You are given a price[] array where price[i] represents the market value of a piece of length i.

2. Examples Provided

The image uses three examples to show how different price structures change the optimal cutting strategy:

<img width="748" height="202" alt="image" src="https://github.com/user-attachments/assets/ff31c37a-705f-4a16-b566-cd658341d2af" />

3. Dynamic Programming Approach (Bottom-Up)
  
The image describes an efficient solution using Tabulation (filling a dp table from the bottom up): Efficiency: The algorithm runs in O(n^2) time and uses O(n) space.The Logic: To find the max value for a rod of length i, you iterate from 1 to n. For each length, you try cutting it into two pieces of lengths j and (i-j) to see which combination yields the highest profit.Storage: Each result is stored in a dp table so you don't have to recalculate the same lengths multiple times.

**Python Implementation: Rod Cutting**
```python
def cut_rod(price):
    n = len(price)
    # Initialize a DP table of size n+1 with zeros
    # dp[i] will store the maximum profit for a rod of length i
    dp = [0] * (n + 1)

    # Build the table from the bottom up
    for i in range(1, n + 1):
        max_val = -1
        # Check every possible cut for a rod of length i
        for j in range(1, i + 1):
            # price[j-1] is the value of a piece of length j
            # dp[i-j] is the pre-calculated best value for the remainder
            max_val = max(max_val, price[j-1] + dp[i-j])
        
        dp[i] = max_val

    return dp[n]

# Example from the image
rod_prices = [1, 5, 8, 9, 10, 17, 17, 20]
print(f"Maximum Profit: {cut_rod(rod_prices)}") 
# Output: 22
```

How the Logic Translates
- The Outer Loop (i): This loop moves through every possible rod length from 1 up to n. By the time we calculate a longer rod, all shorter lengths are already optimized in the dp list;
- The Inner Loop (j): This represents the "cut." For a rod of length i, we try cutting off a piece of length j and adding it to the best known profit for the remaining length (i - j);
- The max() Function: This is the heart of DP. It compares the current best value for length i against the new combination being tested.

Complexity Analysis
- Time Complexity: O(n^2) because of the nested loops used to check every cut for every length;
- Space Complexity: O(n) because we only need a single array to store the maximum values for each length.
