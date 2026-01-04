**Before getting into dymanic programming, a little bit about merge sort**

Merge sort is a recursive algorithm, much like the QuickSort algorithm. First, the array is divided into two from the midpoint, and these two arrays are sorted within themselves. Unlike QuickSort, when these two groups are created within the array, they are not separated based on being smaller or larger than a specific number (pivot). To perform the sorting process, the array continues to be divided into two until it reach single-element pieces. Then, using temporary arrays, these elements are brought back together in a sorted manner.

![merge sort](https://github.com/user-attachments/assets/b56ec814-0d86-489f-990e-1163056219c5)

**the fundamental steps of the Merge Sort**
- turning an unsorted array into a sorted one;
- divides the array into recursively;
- after reducing it to the smallest state, it merges by comparing.

![merge sort2](https://github.com/user-attachments/assets/d9882c57-44b1-47a0-96f1-3ac421c42f2b)

### Algorithm Mergesort(A[0..n-1])

```python
// sorts array A[0..n-1] by recursive mergesort
// input: an array A[0..n-1] of orderable elements
//output: array A[0..n-1] sorted in nondecreasing order
if n > 1
  copy A[0..[n/2] - 1] to B[0..[n/2] - 1]
  copy A[0..[n/2] - 1] to C[0..[n/2] - 1]
  Mergesort(B[0..[n/2] - 1]
  Mergesort(C[0..[n/2] - 1]
  Merge(B, C, A)
```

### Merge(B[0..p-1], C[0..q-1], A[0..p+q-1])

```python
// merge two sorted arrays into one sorted array
// input: array B[0..p-1] and C[0..q-1] both sorted
// output: sorted array A[0..p+q-1] of the elemets of B and C i<-0; j<-0; k<-0
while i < p and j < q do
  if B[i] <= C[j]
    A[k] <- B[i]; i <- i + 1
  else A[k] <- C[j]; j <- j + 1
  k <- k + 1
if i = p
  copy C[j..q-1] to A[k..p+q-1]
else copy B[i..p-1] to A[k..p+q-1]
```

### The mathematical performance of the algorithm
- Recurrence Relation: For n > 1, the relationship is defined as C(n) = 2C(n/2) + C_merge(n), where C(1) = 0
- merge step (C_merge(n)):
  - a comparison is made at every step as long as array indices are being decremented;
  - worts case: this occures when one array still has elements left while the other is just about to empty. In this case, C_merge(n) = n - 1;
  - the worst-case recurrence formula is: C_worst(n) = 2 * C_worst(n/2) + n - 1;
- master theorem apllication:
  - using the master theorem parameters a = 2, b = 2, d = 1;
  - the resulting complexity is: C_worst(n) in Theta(n log n).
 
![master theorem](https://github.com/user-attachments/assets/9beefd39-cbe0-4d5e-a993-1f8bfed5bf47)

### Explanation of TimSort

TimSort is a hybrid sorting algorithm optimized for real-world data, used in major programming languages like python (list.sort, sorted) and java (Arrays.sort(Object[])). It combines the advantages of Insertion Sort and Merge Sort.

What is Timsort? It uses Insertion Sort for small sub-arrays (usually between 32 - 64 elements), and detects ordered blocks in the data (called runs) and merges these blocks using Merge Sort. Because real-world data is often not completely random, Tinsort works very quickly by utilizing this structural information.

**Main Stages of Timsort**
1. Find the ordered blocks (runs) in the data;
2. Sort these blocks using Insertion Sort (if they are short);
3. Combine the ordered blocks using Merge Sort;
4. During the merge, runs are combined according to specific rules (the merge strategy is important).

### Comparing Merge Sort and TimSort

1. Merge Sort is a fundamental sorting algorithm that follows the Divide and Conquer strategy;
2. TimSort is hybrid algorithm that combines Merge Sort and Insertion Sort. It is default sorting method for python and java.

![comparing](https://github.com/user-attachments/assets/f36937df-3869-4216-8e32-25b48829be08)


## Dynamic Programming

Dynamic programming is a method used in computer science, mathematics, economics, and bioinformatics to solve complex problems by breaking them down into overlapping subproblems. It involves solving each subproblem only once and saving this solution to be used later in solving the complex problem.

Key characteristics:
- time efficiency: when a subproblem need to be solved again, the previously saved solution is used, which saves time;
- space-time trade-off: saving these solutions requires more memory space. In other words, dynamic programming algorithms trade space to gain time;
- usage: these algorithms are commonly used in solving optimization problems.

**Fundamentals of dynamic programming**
- a design technique similar to divide-and-conquer;
- in the divide-and-conquer method, subproblems must be independent;
- in dynamic programmingm even if subproblem are not independent, it can still be applied;
- dynamic programming solves each subproblem only once and stores the solution in a table;
- if the same subproblem arises more than oncem it does not re-solve it; instead, it uses the value already stored in the table;
- in this way, the speed of the solution process is inreased.

### Difference between Divide and Conquer and Dynamic programming

![difference](https://github.com/user-attachments/assets/e006cf90-380a-4996-a523-5d8f5629c68f)

examples:
- D&C: Merge Sort, Quick Sort;
- DP: Fibonacci, LCS (Longest Common Subsequence), Knapsack.

### Advantages
- Difficult and complex problems can be solved more easily by breaking them down into interrelated sub-problems using the dynamic programming approach;
- Sequential decision-making advantage is particularly crucial for problems invilving sequential decisions, such as production adjustment and planning;
- Dynamic programming has a flexible structure that can be applied to other mathematical programming problems; therefore, it is more of an optimization approach than just a single technique;
- Integer programming problems and non-linear integer programming problems can be solved using the dynamic programming approach;
- The computational method of dynamic programming allows for the performance of sensitivity analysis.

### Disadvantages

- Dynamic programming has concepts that are harder to understand than other mathematical programming techniques; an expert is definitely needed to comprehend the problem and solve it using an appropriate formula;
- Unlike the Simplex method, it does not have a general algorithm. Because of this, while there are very few software packages written for dynamic programming, these packages are insufficient in most cases or contain significant problems;
- The problem of dimensionality. Having a large number of values for the state variable and decision variable significant increases the size of the tables created for each stage;
- The lack of an effective computational algorithm makes dynamic programming more conceptual than practical in making real dynamic decisions.

### Use cases

Where is it used?

Dynamic programming can be applied to all problems that can be broken down into smaller sub-problems with the same solution structure. However, it shows its true value in problems that would otherwise be solved in exponential time using a brute-force approache. Problems that can be solved with dp:
- rod-cutting problems;
- knapsack problem;
- matrix-chain multiplication;
- assembly line scheduling;
- various string problems: LCS, Longest increasing subsequence, Levenshtein distance.

### Dynamic Programming solution steps
1. Define the problem:
   - identify the repeating sub-problems and the optimal subtructure within the problem.
2. Determine States:
   - express the state of each sub-problem with a variable.
3. Find the transition formula:
   - establish a relationship (recurrence relation) that combines the solutions of the sub-problems.
4. Use a table or memory structure:
   - design a table or array to store the results of the sub-problems.
5. Extract the result:
   - build the solution to the main problem from the solution of all the sub-problems.
  
 ### How is the memoization technique used in dynamic programming?

Dynamic programming helps solve problems with overlapping sub-problems and optimal substructure properties efficiently. The core idea is to break the problem into smaller sub-problems and save the result for future use, thereby eliminating the need to re-calculate the result repeatedly. There are two approaches to formulating a dynamic programming solution:

1. Top-Down Approach

This approach follows the memoization technique. It consists of recursion and caching operations. In the calculation, recursion reoresents the process of calling functions repeatedly, while the cache represents the process of storing intermediate results.

2. Bottom-Up Approach

This approach uses the tabulation technique to implement the dynamic programming solution. It addresses the same issues but without recursion. In this approach, iteration replaces recursion. Consequently, there is no stack overflow error or the additional overhead of recursive procedures. 
    
![dp](https://github.com/user-attachments/assets/1e9aee03-16c9-48b4-922e-dbc2ede30694)

### Tabulation and Memory in dynamic programming

Tabulation and memory (storage) are two techniques used to implement dynamic programming. Both techniques are used when there are overlapping sub-problems. Below is a general overview of the two approaches:

**Memoization**:
- top-down approach: starts with the main problem and breaks it down;
- stores results in a table: saves the outcomes of function calls in a lookup table;
- recursive application: uses recursion to solve the problem;
- on-demend filling: entries are filled into the records only when they are needed.

**Tabulation**:
- bottom-up approach: starts with the smallest sub-problems and builds up to the main goal;
- stores results in a table: deposits the results of sub-problems into a table;
- iterative application: uses loops (iterarion) instead of recursion;
- sequential filling: records are filled from the smallest dimension toward the final dimension in a bottom-up manner.

![dp1](https://github.com/user-attachments/assets/b5d83298-619d-4659-9236-ab77e285413c)

### Code implementation for calculating Fibonacci Numbers using three different methods

Method 1: Naive Recursive
```python
# time complexity: O(2^n)

def fib(n):
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2)
```

Method 2: Memoization (Top-Down)
```python
# time complexity: O(n)
# space: O(n) include call stack and dictionary

memo = {}
def fib(n):
  if n in memo:
    return memo[n]
  if n <= 1:
    return n
  memo[n] = fib(n-1) + fib(n-2)
  return memo[n]
```

Method 3: Tabulation (Bottom-Up)
```python
# time complexity: O(n)
# space: O(n)

def fib(n):
  dp = [0, 1]
  for i in range(2, n+1):
    dp.append(dp[i-1] + ap[i-2])
  return dp[n]
```

```python
# alternative: space optimized
# time complexity: O(n)
# space: O(1)

def fib(n):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return a
```

### LCS Algorithm (Longest Common Subsequence)

The LCS algorithm is a dynamic programming-based algorithm used to find the longest common subsequence between two sequences.

**Basic concepts**

A new sequence obtained by deleting some elements from a sequence without changing their original order. A subsequence that appears in both sequences in the same order. The longest one among all common subsequences.
