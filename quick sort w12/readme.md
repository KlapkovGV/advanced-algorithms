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
   - pivot is in the correct posotion.
   
