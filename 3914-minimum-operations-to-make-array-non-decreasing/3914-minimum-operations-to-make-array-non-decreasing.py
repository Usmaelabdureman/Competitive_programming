class Solution:
    def minOperations(self, nums: list[int]) -> int:
        total_cost = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                total_cost += nums[i] - nums[i + 1]
        return total_cost