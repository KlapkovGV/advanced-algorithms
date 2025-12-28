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

