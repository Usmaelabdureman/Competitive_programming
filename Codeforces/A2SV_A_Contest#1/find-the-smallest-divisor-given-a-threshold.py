from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divide_sum(divisor):
            return sum((num + divisor - 1) // divisor for num in nums)
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if divide_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid
        return left
    