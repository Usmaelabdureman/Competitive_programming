class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentmax, maxSoFar = 0, -inf
        for number in nums:
            currentmax = max(number, currentmax + number)
            maxSoFar = max(maxSoFar, currentmax)
        return maxSoFar