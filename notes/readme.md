### Computatuion Math Challenges

**The strong number challenge**

Concept: verify if a number equals the sum of its digits's factorial.

```python
def is_strong_numner(n):
  digit_sum = sum(math.factorial(int(digit)) for digit in str(n))
  return digit_sum == n
```

**The Lucas Sequence Generator**

Concept: A variation of the Fibonacci sequence starting with L_0 = 2 and L_1 = 1.

output: finding the nth element

```python
def generate lucas(n_terms):
  lucas = [2, 1]
  while len(lucas) < n_terms:
    lucas.append(lucas[-1] + lucas[-2])
  return lucas
```

___

### Algorithm Analysis 

**Asymptotic Notation guide**

O(n) provies an upper bound, not a strict equality of steps.
- Big O (upper bound): the "worst-case" scenario;
- Big Omega (lower bound): the "best-case" scenario;
- Big Theta (tight bound): when the upper and lower bounds meet.

**Complexity tracker**

```python
def analyze_complexity(data_size):
  op_counter = 0

  # triple nested loop structure
  for x in range(data_size):
    op_counter += x
    for y in range(data_size):
      for z in range(data_size):
        op_counter += x

  # separate double nested loop
  for x in range(data_size):
    for y in range(data_size):
      op_counter += x

  return op_counter

# testing
for n in [10, 20, 30]:
  total_ops = analyze_complexity(n)
```

The code consists of two main blocks:
1. the triple nest: we have a loop for x, inside a loop for y, and inside that a loop for z. In big-O notation, nested loops are multiplicative. Since there are three levels of nesting dependent on n, this block performs approximately n^3 operations.
   - complexity: O(n^3)
2. the double nest: a seperate set of loops for x and y follows the first block. This performes n^2 operations.
   - complexity: O(n^2)

In asymptotic analysis, we only keep the highest-order team because it dominates the growth as n approaches infinity.

O(n^3) + O(n^2) = O(n^3)

**Binary Search Comparisons**

Given a sorted array of 16 elements: [1, 4, 9, 15, 19, 22, 28, 33, 40, 47, 52, 59, 66, 73, 85, 94]. How many comparisons are needed to find if the number 16 exists?
- step 1: check middle (index 7, value 33). 16 < 33, go left
- step 2: check middle of left half (index 3, value 15). 16 > 15, go right
- step 3: check middle of remaining (index 5, value 22). 16 < 22, go left
- step 4: check remaining (index 4, value 19). 16 not equals to 19. Search ends

Python implemantation
```python
def binary_search_count(arr, target):
  low = 0
  high = len(arr) - 1
  count = 0
  while low <= high:
    count += 1
    mid = (low + high) // 2
    if arr[mid] == target:
      return count
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return count
```

**Matrix multiplication complexity**

1. For **square matrices** of size n x n the standard triple-loop algorithm requires approximately:
   - n^3 multiplications
   - n^3 additions
   - total: **O(n^3)** floating-point operations
  
2. For rectangular matrices p x q and q x r operation count:
  - multiplication = p * q * r,
  - additions = p * r * (q - 1)

3. Faster algorithms

Asymptotically better methods exist:
- Strassen's algorithm: O(n^2.81)
- modern algorithms (theoretical): down to O(n^2.373)


___

### Data Structures & Logic

**Array indexing**
- zero-based indexing: for an array of size N, the range is always 0 to N-1

**Representing logic**

The transition from natural language (algorithm steps) to pseudocode to source code.

___

### Algorithm Design Theory

Concept: Algorithm characteristics to be valid, an algorithm must possess specific properties that ensure it can be executed reliably.
- definiteness (clarity): every step must be precisely defined and unambiguous;
- finiteness: the process must teminate after a countable number of steps;
- efficiency: the algorithm should use resoueces (time/memory) effectively.

Concept: Definition of an Algorithm
- "An algorithm is any well-defined computational procedure that takes some value, or set of values, as input and produces some value, or set of values, as output". Cormen, Thomas H., et al. Introduction to Algorithms. 3rd ed., The MIT Press, 2009.
- key distinction: while a program is the implementation, the algorithm is the logical sequence of steps itself.

___

### Recursive computation

Challenge: combined recursive functions. This demonstrates how to calculate the sum of two different recursive mathematical sequences at a specific point n.
- function F(n) (Factorical): defined as n x F(n-1).
- function G(n) (Fibonacci): defined as G(n-1) + G(n-2)
- solution: F(n) + G(n)

___

### Algorithm Optimization Strategies

Concept: A Greedy approach makes the best local choice at each step without reconsidering previous decisions.
- local optimum: it focuses on the immediate best result;
- irreversibility: once a choice is made, it is never reversed;
- selection vs. systematic search: it does not try every possible solution (which would be Brute Force); it follows a specific heuristic;
- real-world examples: selection sort and huffman codding.


