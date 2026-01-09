def knapsack_01(values, weights, capacity):
  '''
  0/1 knapsack problem: each item can be taken at most once
  returns maximum value that can be obtained

  Args:
    values: list of item velues
    weights: list of item weights
    capacity: maximum weight capacity of knapsack
  '''
  n = len(values)
  # create DP table
  dp = [[0] * (capacity + 1) for _ in range(n + 1)]

  # build DP table
  for i in range(1, n + 1):
    for w in range(1, capacity + 1):
      if weights[i-1] <= w:
        dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
      else:
        dp[i][w] = dp[i-1][w]

  selected_items = []
  w = capacity
  for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
      selected_items.append(i-1)
      w -= weights[i-1]

  return dp[n][capacity], selected_items[::-1]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected = knapsack_01(values, weights, capacity)
