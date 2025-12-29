## Quick Sort Algorithm

It is efficient, recursive, divide-and-conquer sorting algorithm. If works by selecting a "pivot" element from the array and partitioning the remaining elements into sub-arrays:
- those with elements smaller than the pivot;
- those with elements larger than the pivot.

The process is then applied recursively to the sub-arrays.

How algorithm works

1. Select an element from the array as a pivot. Commonly:
   - first element;
   - last element;
   - random element;
   - median of three elements;
   - the ninether method.
2. Rearrange the array as follows:
   - items smaller than the pivot are on the left;
   - items larger than the pivot are on the right (naive, lomuto);
   - pivot is in the correct position.
3. Apply the algorithm recursively to the sub-array to the left and right of the pivot;
4. Stop when there are fewer than two elements in the array.

Time complexity:
- best/average case: O(n log n) - when the pivot divides the array equally;
- worst case: O(n^2) - when the pivot is consistently the smallest or larger element, leading to unbalanced partitions (for example, when the array is already sorted and the first/last element is chosen as the pivot).

Space complexity:
- In-place implementation: O(log n) (stack space for recursion).

  ![quick sort](https://github.com/user-attachments/assets/6e99adf6-bf51-4410-ab60-6b3eea34aa96)

1. Select a Pivot: Select an item from the array as a pivot.
2. Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on ist left, and all elements larger then the pivot will be on its right. The pivot is then in the correct position and we obtain the pivot's index.
3. Apply same process recursively to the two partitioned sub-arrays (to the left and right of the pivot).
4. When only one element remains in the sub-array, recursion stops because a single element is already sorted.

Naive partition algorithm

It is a simple method that generally performs the process of dividing arrays or sets into smaller pieces. This algorithm is generally less efficient compared to more complex and optimized algorithms, but it can be used as a simple approach to obtain a solution for a specific problem.

General Structure of the algorithm

1. Take an array;
2. Divide this array into two;
3. This process is repeated in the same way for each part.

In general, it is similar to the partitioning step used in the quick sort algorithm. However, naive partition usually works in a simpler, less optimized way.

Disadvantages of Naive Partition:
- this algorithm is generally not very efficient because, in most cases, it performs more operations than better-optimized algorithms;
- time compexity can generally be O(n^2) because it may be necessary to compare elements one by one to divide the array properly ay each step.

Naive Partition algorithm can be used in small datasets or applications that do not require optimization.

```python
def naive_partition(arr, low, high):
   # Select a pivot
   pivot = arr[high]

   # Create a new (extra) array to hold partitioned elements
   temp = [0] * (high - low + 1)
   index = 0

   # Add smaller elements to the new array
   for i in range(low, high + 1):
      if arr[i] < pivot:
         temp[index] = arr[i]
         index += 1

   # Add equal elements (including the pivot)
   new_pivot_index = index + low
   for i in range(low, high + 1):
      if arr[i] == pivot:
         temp[index] = arr[i]
         index += 1

   # Add larger elements
   for i in range(low, high + 1):
      if arr[i] > pivot:
         temp[index] = arr[i]
         index += 1

   # Copy the partitioned elements back into the original array
   for i in range(len(temp)):
      arr[low + i] = temp[i]

return new_pivot_index

list = [3, 7, 8, 5, 2, 1, 9, 5, 4]
pivot_idx = naive_partition(list, 0, len(list) - 1)
```

Characteristics of this code:
- it iterates through the array multiple times to group elements smaller than, equal to, and larger than the pivot;
- is uses a temp list of size O(n);
- unlike optimized versions, it simply copies values into a new structure.

**Lomuto Partition**
- pivot is the last element;
- smaller elements are kept on the left;
- a swap is performed every time a smaller element is found.

Easy to code and the pivot ends up in the correct spot. But algorithm performes a lot of swaps and identical elements decrease performance.

```python
def lomuto_partition(arr, low, high):
   # pivot is the last element
   pivot = arr[high]

   i = low - 1

   for j in range(low, high):
      if arr[j] <= pivot:
         i += 1
         arr[i], arr[j] = arr[j], arr[i]

   arr[i + 1], arr[high] = arr[high], arr[i + 1]

   return i + 1

list = [3, 7, 8, 5, 2, 1, 9, 5, 4]
pivot_idx = lomuto_partition(data, 0, len(data) - 1)
```

