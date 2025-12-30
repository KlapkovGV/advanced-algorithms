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

**Hoare Partition**
- pivot is the first element;
- two pointers are used (from the left and from the right);
- elements in the wrong place are swapped;
- the process ends when the pointers cross each other.

This algorithm fast, has fewer swaps, and ideal for large arrays. Although, algrothm logic has more complex logic.

```python
def hoare_partition(arr, low, high):
   pivot = arr[low]

   # initialize left (i) and right (j) pointers. They start outside the range and move inward
   i = low - 1
   j = high + 1

   while True:
      i += 1
      while arr[i] < pivot:
         i += 1

      j -= 1
      while arr[j] > pivot:
         j -= 1

      arr[i], arr[j] = arr[j], arr[i]

list = [3, 7, 8, 5, 2, 1, 9, 5, 4]
split_point = hoare_partition(list, 0, len(list) - 1)
```

Efficiency of the algorithm is considered very fast because it performs fewer swaps on average. 

**Comparison of Partitioning Methods**

| Feature | Naive | Lomuto | Hoare |
| :--- | :---: | :---: | :---: |
| **Extra Array** | + | - | - |
| **In-place** | - | + | + |
| **Swap Count** | 0 | High | Low |
| **Pivot Position** | Middle | Correct Spot | Uncertain |
| **Performance** | Low | Medium | High |
| **Suitability for Quick Sort** | - | + | ++ |   

**Median of three algorithm**

A simple but effective method used to improve pivot selection in quick sort. Three elements are selected (typically the first, middle, and last elements). The median (or middle value) of these three is chosen as the pivot. It proposes to prevent poor pivot selection and to achieve a more balanced partition. 

To improve Quick Sort implementation, we can use the Median of Three logic to select a better pivot, which helps avoid the O(n^2) worst-case performance. 

This method selects three elements - the first, middle, and last - and uses their median value as the pivot.

```python
def get_median_pivot(arr, low, high):
   mid = (low + high) // 2

   # sort elements to find the median
   if arr[mid] < arr[low]:
      arr[low], arr[mid] = arr[mid], arr[low]
   if arr[high] < arr[low]:
      arr[low], arr[high] = arr[high], arr[low]
   if arr[high] < arr[mid]:
      arr[mid], arr[high] = arr[high], arr[mid]

   # the median is now at arr[mid]. We can swap it with arr[high] to use with Lomuto Partition
   arr[mid], arr[high] = arr[high], arr[mid]
   return arr[high]

def quick_sort(arr, low, high):
   if low < high:
      # pick better pivot
      get_median_pivot(arr, low, high)

      # partition the array using the selected pivot
      p = lomuto_partition(arr, low, high)

      # recursively sort left and right parts
      quick_sort(arr, low, p - 1)
      quick_sort(arr, p + 1, high)
```

![quick sort](https://github.com/user-attachments/assets/61565274-c547-4629-b966-c1d30a1de433)

to understand why we use p - 1 and p + 1 in the recursive calls

This Divide and Conquer approach continues until the entire array matches the final sorted result: [1, 2, 3, 4, 5, 5, 7, 8, 9]

**The Ninther**

This method is an advanced technique used to select a better pivot in Quick Sort.

The Ninther method determines a pivot by selecting 9 elements from the array:
- first, it calculates three median of three values from these elements;
- then, it takes the median of these 3 medians to determine the final pivot.

It useful to achieve a more balanced partition and to reduce the probability of the worst-case scenario.

Why is it necessary? 

The performance of Quick Sort is highly dependent on pivot selection:
- poor pivot results to O(n^2) complexity;
- good pivot results to O(n log n) complexity.
- the Ninther is much more reliable than simple methods like piking the first or last element as the pivot.

Here is an implementation showing how the Ninther is used to select a pivot
```python
def get_median_of_three(arr, a, b, c):
   """Helper to find the median of three elements"""
   if (arr[a] < arr[b]):
      if (arr[b] < arr[c]): return b
      if (arr[a] < arr[c]): return c
      return a
   else:
      if (arr[a] < arr[c]): return a
      if (arr[b] < arr[c]): return c
      return b

def get_ninther(arr, low, high):
   """Implements Tukey's Ninther: Divide 9 elements into 3 groups of 3, find their medians, then find the median of those 3 medians."""
   length = high - low + 1
   gap = length // 8

   # select 9 spread-ot indices
   # m1, m2, m3 are the medians of the three groups
   m1 = get_median_of_three(arr, low, low + gap, low + 2 * gap)
   m2 = get_median_of_three(arr, low + 4 * gap, low + 5 * gap, low + 6 * gap)
   m3 = get_median_of_three(arr, high - 2 * gap, high - gap, high)

   # return the index of the median of the three medians
   return get_median_of_three(arr, m1, m2, m3)

def quick_sort_ninther(arr, low, high):
   if low < high:
      # choose pivot using Ninther strategy
      pivot_idx = get_ninther(arr, low, high)

      # move pivot to the end for partitioning
      arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

      # partition
      pivot = arr[high]
      i = low - 1
      for j in range(low, high):
         if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
      arr[i + 1], arr[high] = arr[high], arr[i + 1]

      p = i + 1

      # recursive calls
      quick_sort_ninther(arr, low, p - 1)
      quick_sort_ninther(arr, p + 1, high)

list = [42, 7, 101, 15, 33, 5, 88, 2, 56, 11, 9, 24, 67, 1]
quick_sort_ninther(data, 0, len(list) - 1)
```

Note that using the Ninther on a tiny array (like 5 elements) would result in index errors or redundant work.




