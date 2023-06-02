def max_subsequence(nums):
  currentmax, maxSoFar = 0, float('-inf')
  for number in nums:
      currentmax = max(number, currentmax + number)
      maxSoFar = max(maxSoFar, currentmax)
  return maxSoFar
