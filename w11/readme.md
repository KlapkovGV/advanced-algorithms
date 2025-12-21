## Divide and Conquer algorithms

A Problem is solved recursively by applying three steps at each level of the recursion.

Steps: 

Divide the problem into a number of subproblems that are smaller instances of the same problem.

Conquer the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner.

Combine the solutions to the subproblems into the solution for the original problem. 

![divide and conquer](https://github.com/user-attachments/assets/38a2a26f-4635-4e1f-aa18-1793ab80e3c9)

**Advantages**

- Divide and Conquer algorithms produce more efficient solutions for many problems, e.g., O(n log n) (linearithmic) instead of O(n^2) (quadratic). For examples, Merge Sort with O(n log n), Quick Sort (average case) with O(n log n), and Binary Search with O(log n) times complexity. 

- This approach divides complex problems into understandable subproblems. Makes the code logically cleaner and more modular. 

- The Divide and Conquer structure is ideal for recursive functions. Mathematical analysis of the algorithm can be done more systematically (e.g. using the Master Theorem).

- Since subproblems can often be solved independently on multi-core systems and in distributed systems. They can be executed in parallel.

- The time complexity can often be written in the form: T(n) = a*T(n/b) + f(n), where a is number of subproblems, n/b is a size of each subproblems, f(n) is a cost of dividing and combining. This standardizes the analysis.

**Master Theorem** for a recurrence relations: T(n) = a*T(n/b) + f(n), f(n) ∈ Θ(n^d), d >= 0

Statement. If f(n) ∈ Θ(n^d) where d >= 0 in the recurrence then 
- T(n) ∈ Θ(n^d) if a < b^d,
- T(n) ∈ Θ(n^d log n) if a = b^d,
- T(n) ∈ Θ(n^log_b a) if a > b^d.

Here a = 4, b = 2:

1. f(n) = n -> d = 1

   Compare a and b^d: 4 vs 2^1 ->  a > b^d -> T(n) ∈ Θ(n^log_2 4) = Θ(n^2)

2. f(n) = n^2 -> d = 2

   b^d = 2^2 = 4, a = 4 -> a = b^d -> T(n) ∈ Θ(n^2 log n)

3. f(n) = n^3 -> d = 3

   b^d = 2^3 = 8, a = 4 -> a < b^d -> T(n) ∈ Θ(n^3)
