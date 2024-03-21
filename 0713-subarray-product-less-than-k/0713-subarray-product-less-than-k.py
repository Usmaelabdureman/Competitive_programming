class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        count = 0
        left = 0 
        prod = 1

        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1
        return count
