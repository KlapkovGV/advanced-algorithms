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



    
