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

The Master Method can be used to determine the running time of the divide and conquer algorithm for the maximum subarray problem as well as for matrix multiplication.

**Disadvantages**

- Recursive calls use extra space in the memory stack. If the recursion goes too deep, the program will crash with a Stack Overflow error.
  
- Recursion can lead to redundant calculations if subproblems are not independent.
  
- Some algorithms, like Merge Sort, require O(n) extra memory.

**Comparing two different methods for finding the maximum value in a dataset: Linear Search and Divide and Conquer**

Linear Search checks every element one by one from the beginning to the end of the array to find the largest one.

 - Time Complexity: O(n)
 - Memory Usage: O(1)
 - Performance (CPU & RAM):
      - Highly efficient for CPU's because it accesses data sequentially, making it cache-friendly;
      - Uses minimum RAM;
      - Runs very fast on modern processors with optimized code that avoids branching.

Divide and Conquer method divides the array into two parts, finds the maximum in each part separately, and then compares them.

 - Time Complexity: O(n)
 - Memory Usage: O(log n) (due to the recursion stack)
 - Performance (CPU & RAM):
      - Places more load on the CPU due to function call overhead and stack memory usage;
      - Poor cache performance because the data is constantly being divided.

**Lomuto Partition** is one of the best-known partitioning methods used within the Quick Sort algorithm. This method divides an array into two groups by selecting a pivot element.

   - Elements less than or equal to the pivot go to the left.
   - Elements greater than the pivot go the right.

How does it work?

1. The pivot is usually selected as the last element of the array.
2. i pointer: used to keep track of the elements smaller than pivot.
3. j pointer: used to traverse the array.
4. if j finds an element smaller than the pivot, it swaps with i.
5. Finally, the pivot swaps with i+1, and the partitioning is complete.


