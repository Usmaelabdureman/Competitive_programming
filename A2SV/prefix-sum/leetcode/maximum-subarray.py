class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum < 0:
                curr_sum = 0
            max_sum = max(curr_sum,max_sum)
        return max_sum if max_sum > 0 else max(nums)
        