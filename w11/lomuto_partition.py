def lomuto_partition(A, l, r):
  p = A[l]
  s = l

  for i in range(l+1, r+1):
    if A[i] < p:
      s = s + 1
      A[s], A[i] = A[i], A[s]

  # swapping
  A[l], A[s] = A[s], A[l]

  return s

# Example usage:
arr = [4, 2, 8, 1, 3]
pivot_index = lomuto_partition(arr, 0, len(arr) - 1)
